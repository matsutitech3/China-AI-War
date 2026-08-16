#!/usr/bin/env python3
"""Cost model: capacity-first local appliance vs Rubin NVL72 central serving, Kimi K3.
All memory prices on a pre-surge (mid-2025) basis, per the book's stated assumption.
Run: python3 appliance-vs-rubin.py
"""
import math

# ---------------- Kimi K3 architecture (Moonshot model card / arXiv 2607.24653) --------------
TOTAL_P   = 2.8e12
ACTIVE_P  = 104e9
N_EXP     = 896
K_EXP     = 16
BYTES_PER_PARAM = 0.5           # MXFP4 (ignoring scale overhead)
NONEXP_ACTIVE_P = 55e9          # attention + shared experts + embeddings read every step (est.)
EXP_P     = (ACTIVE_P - NONEXP_ACTIVE_P) / K_EXP   # ~3.06B per routed expert
GB = 1e9
per_expert_gb = EXP_P*BYTES_PER_PARAM/GB
nonexp_gb     = NONEXP_ACTIVE_P*BYTES_PER_PARAM/GB
KV_PER_TOKEN_FP8 = 13.8e3       # bytes (24 MLA layers, kv_lora 512+rope 64, FP8)
KDA_STATE_PER_SEQ = 207e6       # bytes (69 KDA layers, BF16)

def distinct_experts(B):        # uniform independent routing (pessimistic)
    return N_EXP*(1-(1-K_EXP/N_EXP)**B)

def step_bytes_gb(B):
    return nonexp_gb + distinct_experts(B)*per_expert_gb

# ---------------- Appliance configuration -----------------------------------------------------
HBF_STACKS      = 4             # 4 x 512 GB gen-1 = 2 TB
HBF_BW_PER_STACK= 1.6e12        # SanDisk gen-1 fact sheet
HBF_BW          = HBF_STACKS*HBF_BW_PER_STACK
LPDDR_GB        = 256
LPDDR_BW        = 900e9         # ~512-bit LPDDR6X
SOC_FP4_DENSE   = 400e12        # achieved dense FP4 for prefill (GB10-class ~1 PF sparse)

def per_user_tps(B):
    return HBF_BW/ (step_bytes_gb(B)*GB)

# ---------------- BOM (pre-surge memory basis) -------------------------------------------------
# Every component is anchored to a finished, shipping, pre-surge (mid-2025) system,
# not to a bare-component guess:
#   - DGX Spark (GB10, "up to 1 PFLOP FP4" sparse, 128GB LPDDR5X): ASUS Ascent GX10
#     partner box $2,999 at launch; NVIDIA Founders Edition $3,999 before the Feb-2026 rise.
#   - Framework Desktop (AMD Ryzen AI Max+ 395, 128GB LPDDR5X): $1,999 at announcement;
#     GMKtec EVO-X2 on the same silicon $1,799.99 early-bird.
#   - 1TB NVMe retail, pre-surge: roughly $65-100 in Q1 2025, $45-90 in late 2025
#     (storagediskprices.com, tech-insider.org) -- a *finished* product carrying a
#     controller ASIC, PCB, connector, enclosure and full retail margin, none of which
#     a bare HBF stack carries (no controller, no PCIe: read directly over UCIe).
#   - HBF, 512GB gen-1 stack: "a couple hundred dollars at most" is the stated floor,
#     consistent with the die-cost arithmetic already in the text (mid-2025 TLC NAND
#     spot ~$0.042/GB => ~$21 of raw die for 512GB, plus TSV stacking, logic die and
#     test) and consistent with undercutting a finished 1TB NVMe retail unit despite
#     the added packaging step, because it skips the controller/PCB/enclosure/margin
#     stack a retail SSD carries.
cases = {
 'optimistic': dict(hbf_stack=150, lpddr_gb=3.3,  soc=500,  pkg=600, rest=300, margin=0.25),
 'base':       dict(hbf_stack=200, lpddr_gb=3.8,  soc=650,  pkg=700, rest=400, margin=0.30),
 'conservative':dict(hbf_stack=250, lpddr_gb=4.5, soc=850,  pkg=800, rest=550, margin=0.40),
}
def price(c):
    bom = HBF_STACKS*c['hbf_stack'] + LPDDR_GB*c['lpddr_gb'] + c['soc'] + c['pkg'] + c['rest']
    return bom, bom/(1-c['margin'])

# ---------------- Appliance power ---------------------------------------------------------------
HBF_PJ_BIT   = 7.0              # ~2x HBM4 (est. 3.5 pJ/bit)  -> ~360 W at 6.4 TB/s
P_HBF_FULL   = HBF_BW*8*HBF_PJ_BIT*1e-12
P_SOC_FULL   = 200.0
P_OTHER_FULL = 60.0
P_FULL       = P_HBF_FULL + P_SOC_FULL + P_OTHER_FULL
P_IDLE       = 45.0             # HBF non-volatile: no refresh; LPDDR self-refresh + SoC idle
TARIFF_COMM  = 0.135            # $/kWh US commercial (EIA May 2026)
AMORT_YRS    = 4
MAINT_FRAC   = 0.03             # per year of price

# ---------------- Rubin VR200 NVL72 central serving ------------------------------------------
RACK_PRICE   = 7.8e6            # Morgan Stanley BoM estimate (May 2026)
RACK_KW      = 210              # ~1.8-2.3 kW/GPU
PUE          = 1.2
TARIFF_HYPER = 0.075
OPEX_OTHER   = 450e3            # facility, network, staff, per rack-year
UTIL         = 0.60
TPS_PER_GPU  = {'throughput (~25 tok/s/user)': 3000, 'interactive parity (~50 tok/s/user)': 1800}

def central_cost_per_M(mode, amort=4):
    tps = TPS_PER_GPU[mode]*72
    tokens_yr = tps*UTIL*365*86400
    cost_yr = RACK_PRICE/amort + RACK_KW*PUE*8760*TARIFF_HYPER + OPEX_OTHER
    return cost_yr/(tokens_yr/1e6), cost_yr, tokens_yr

# ---------------- API prices, $/M output tokens (Aug 2026) --------------------------------------
api = {'Claude Opus 5 (AA 63)':25, 'GPT-5.6 Sol (AA 61)':30, 'Grok 4.6 (AA 61)':6,
       'Gemini 3.1 Pro':12, 'Kimi K3 API (AA 60)':15, 'Qwen3.8-Max':6,
       'DeepSeek V4-Pro (peak/off-peak)':(3.96,1.98)}

if __name__=='__main__':
    print(f"per routed expert: {per_expert_gb:.2f} GB; non-expert per step: {nonexp_gb:.1f} GB; batch-1 step: {step_bytes_gb(1):.1f} GB")
    print("\n--- Appliance decode throughput (uniform routing, 6.4 TB/s HBF) ---")
    for B in [1,2,3,4,6,8,16]:
        print(f" B={B:2d}: distinct experts {distinct_experts(B):6.1f}  step {step_bytes_gb(B):6.1f} GB  per-user {per_user_tps(B):5.1f} tok/s  aggregate {B*per_user_tps(B):6.1f}")
    B=4; agg = B*per_user_tps(B)
    kv_bw = B*per_user_tps(B)*128e3*KV_PER_TOKEN_FP8
    print(f"\n KV traffic at B=4, 128K ctx, FP8: {kv_bw/1e9:.0f} GB/s of {LPDDR_BW/1e9:.0f} GB/s LPDDR6X")
    print(f" KV+state footprint, 8 seqs @128K: {(8*128e3*KV_PER_TOKEN_FP8+8*KDA_STATE_PER_SEQ)/1e9:.1f} GB")
    prefill_128k = 128e3*ACTIVE_P*2/SOC_FP4_DENSE
    print(f" prefill 128K prompt at {SOC_FP4_DENSE/1e12:.0f} TFLOPS dense: {prefill_128k:.0f} s; 32K: {prefill_128k/4:.0f} s")
    print(f"\n--- Appliance power: full {P_FULL:.0f} W (HBF {P_HBF_FULL:.0f}), idle {P_IDLE:.0f} W; energy {P_FULL/agg:.2f} J/token ---")
    print("\n--- BOM and price ---")
    for k,c in cases.items():
        bom,p = price(c); print(f" {k:13s} BOM ${bom:,.0f}  price ${p:,.0f}")
    print("\n--- Appliance cost per M output tokens (base price) ---")
    _,pbase = price(cases['base'])
    for label, mo_tokens in [('50M/mo',50e6),('100M/mo',100e6),('300M/mo',300e6),('capacity',agg*30*86400)]:
        E_kwh = (mo_tokens*P_FULL/agg + P_IDLE*(720*3600 - mo_tokens/agg))/3.6e6
        cost_mo = pbase/(AMORT_YRS*12) + pbase*MAINT_FRAC/12 + E_kwh*TARIFF_COMM
        print(f" {label:9s}: {mo_tokens/1e6:6.0f} M tok  power {E_kwh:5.0f} kWh  cost ${cost_mo:6.0f}/mo  = ${cost_mo/(mo_tokens/1e6):5.2f}/M")
    for k in ['optimistic','conservative']:
        _,p=price(cases[k]); mo=100e6
        E_kwh=(mo*P_FULL/agg + P_IDLE*(720*3600-mo/agg))/3.6e6
        cost_mo=p/(AMORT_YRS*12)+p*MAINT_FRAC/12+E_kwh*TARIFF_COMM
        print(f" {k:13s} @100M/mo: ${cost_mo:.0f}/mo = ${cost_mo/100:.2f}/M")
    print("\n--- Rubin VR200 NVL72 central marginal cost ---")
    for mode in TPS_PER_GPU:
        for am in (4,6):
            c,cy,ty = central_cost_per_M(mode, am)
            print(f" {mode:38s} {am}-yr: ${cy/1e6:.2f}M/yr, {ty/1e12:.2f}T tok/yr -> ${c:.2f}/M")
    print("\n--- API list prices, $/M output ---")
    for k,v in api.items(): print(f" {k:32s} {v}")
