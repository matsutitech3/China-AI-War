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
CHECKPOINT_TB = 1.4             # published MXFP4 download for Kimi K3

def distinct_experts(B):        # uniform independent routing (pessimistic)
    return N_EXP*(1-(1-K_EXP/N_EXP)**B)

def step_bytes_gb(B):
    return nonexp_gb + distinct_experts(B)*per_expert_gb

# ---------------- Appliance configuration -----------------------------------------------------
# FOUR first-generation stacks, not two. Two 512 GB gen-1 stacks are 1,024 GB and cannot hold a
# 1,400 GB checkpoint at all; three hold it with ~136 GB spare; four hold it with ~648 GB of
# runtime and cache headroom and are the configuration used everywhere in the text.
HBF_STACKS      = 4             # 4 x 512 GB gen-1 = 2 TB
HBF_BW_PER_STACK= 1.6e12        # SanDisk gen-1 fact sheet
HBF_BW          = HBF_STACKS*HBF_BW_PER_STACK
HBF_CAP_GB      = HBF_STACKS*512
LPDDR_GB        = 256
LPDDR_BW        = 900e9         # ~512-bit LPDDR6X
SOC_FP4_DENSE   = 400e12        # achieved dense FP4 for prefill (GB10-class ~1 PF sparse)

def per_user_tps(B):
    return HBF_BW/ (step_bytes_gb(B)*GB)

# ---------------- BOM (pre-surge memory basis) -------------------------------------------------
# Every non-HBF component is anchored to a finished, shipping, pre-surge (mid-2025) system,
# not to a bare-component guess:
#   - DGX Spark (GB10, "up to 1 PFLOP FP4" sparse, 128GB LPDDR5X): ASUS Ascent GX10
#     partner box $2,999 at launch; NVIDIA Founders Edition $3,999 before the Feb-2026 rise.
#   - Framework Desktop (AMD Ryzen AI Max+ 395, 128GB LPDDR5X): $1,999 at announcement;
#     GMKtec EVO-X2 on the same silicon $1,799.99 early-bird.
#
# HBF stack price is a SCENARIO VARIABLE, not a ceiling, and it is the only thing that moves
# between the three cases below. The three anchors:
#   - optimistic $200/stack: die-cost arithmetic (mid-2025 TLC NAND spot ~$0.042/GB => ~$21 of
#     raw die in 512 GB) plus TSV stacking, logic die and test, on the argument that the stack
#     skips the controller/PCB/enclosure/retail margin a finished SSD carries.
#   - base $500/stack: SanDisk's own "similar cost to HBM per stack", against an HBM4 12-high
#     stack reported at $500-560 in late 2025.
#   - stressed $1,000/stack: a two-vendor first-generation part priced like the scarce component
#     it would be if HBF is adopted at datacentre scale.
# NOTE ON AN INFERENCE THIS MODEL DOES NOT MAKE: a finished 1 TB NVMe SSD at $65-100 retail is
# $0.065-0.100/GB, against $0.293-0.488/GB for a bare 512 GB stack at $150-250. The SSD price
# does not bound the stack price -- packaging, test, yield, host interface and market structure
# all differ -- so the low case is carried as the optimistic scenario and not as a ceiling.
STACK_PRICE = {'optimistic': 200.0, 'base': 500.0, 'stressed': 1000.0}
LPDDR_PER_GB = 3.8              # pre-surge LPDDR5X basis, premium for LPDDR6X
LPDDR_COST   = 973.0            # 256 GB at $3.80/GB, to the dollar
SOC_COST     = 650.0            # GB10-class SoC with UCIe ports
PKG_COST     = 700.0            # 2.5D package carrying SoC + 4 stacks (CoWoS-class estimate)
REST_COST    = 400.0            # board, PSU, chassis, cooling, boot storage
MARGIN       = 0.30             # OEM gross margin, held constant across the three cases
NONHBF_BOM   = LPDDR_COST + SOC_COST + PKG_COST + REST_COST              # $2,723

def price(case):
    bom = HBF_STACKS*STACK_PRICE[case] + NONHBF_BOM
    return bom, bom/(1-MARGIN)

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
# "Server in the closet": what the SME actually adds to an existing server room.
CLOSET_PUE   = 1.3              # small-room air conditioning, worse than hyperscale 1.2 (assumption)
CLOSET_CAPEX = 500.0            # a UPS and a shelf; no new circuit, no new room, no new cooling plant
CLOSET_LIFE  = 10               # years
# Human operation. The machine cost below carries NO labour; it is a MACHINE cost, not a fully
# loaded service cost. An operated service is priced separately, because zero operator-hours is
# an assumption about the agent stack and not an observation.
OPERATOR_RATE = 100.0           # $/hour, loaded cost of an administrator's time
OPS_HOURS     = [0, 1, 4]       # operator-hours per month
WACC         = 0.08             # cost of capital applied to BOTH sides (Meta Hyperion 6.6%, CoreWeave 9-9.75%)

def annuity(r, n):              # annual payment per $1 of capital over n years at rate r
    return r/(1-(1+r)**-n) if r>0 else 1.0/n

# ---------------- Rubin VR200 NVL72 central serving ------------------------------------------
# Rack price. NOTE ON WHAT THIS IS: Morgan Stanley's May-2026 "bill of materials" for the
# VR200 NVL72 is a costed component list at the prices a cloud provider PAYS -- GPUs at ~$55k
# each, i.e. NVIDIA's ASP with its ~75% gross margin already inside -- not NVIDIA's cost of
# goods (PC Gamer's report of the note says so explicitly). It is therefore an end-user
# transaction price for a volume buyer, symmetric with the appliance's retail price (BOM plus
# a 30% OEM margin). Trade reporting (Tom's Hardware, Mar 2026) puts ODM quotes at
# $5-7M without warranty and "as much as $8.8M"; an enterprise or neocloud buying through an
# OEM with warranty and support pays more, and GB300 NVL72 retail has been put as high as
# ~$10M. Both cases are run.
RACK_PRICE       = 7.8e6        # hyperscaler / volume transaction price (Morgan Stanley, May 2026)
RACK_PRICE_RETAIL= 10.0e6       # enterprise / neocloud retail through an OEM, warranty and support
RACK_KW      = 210              # ~1.8-2.3 kW/GPU
PUE          = 1.2
TARIFF_HYPER = 0.075
UTIL         = 0.60
TPS_PER_GPU  = {'throughput (~25 tok/s/user)': 3000, 'interactive parity (~50 tok/s/user)': 1800}
# The building the rack has to live in. Facility capex is per watt of IT load, excluding land
# and the IT itself: Matsuoka (Aug 2026) architecture A "resilient inference/cloud", Tier-III-
# capable, P50 $11.9/W (P10 $8.5, P90 $17.7); Epoch AI (May 2026) $12/W of a $38/W all-in 1 GW
# campus; JLL 2026 shell-and-core $11.3M/MW; Turner & Townsend Silicon Valley $13.3/W (narrower scope).
FAC_CAPEX_W  = {'P10': 8.5, 'P50': 12.0, 'P90': 17.7}
FAC_LIFE     = 15               # years: Epoch uses 14; REIT lives 5-39; MEP 10-25
FAC_OPEX_KW  = 300.0            # $/kW-IT/yr non-energy opex: staff, maintenance, security, insurance,
                                # property tax, water (Epoch $0.3B/GW-yr; KPMG $237-353/kW-yr; ITK ~$320)

def central_cost_per_M(mode, amort=4, util=UTIL, fac='P50', wacc=WACC, rack_price=RACK_PRICE):
    """Fully loaded operator cost per M output tokens for one VR200 NVL72 rack."""
    tps = TPS_PER_GPU[mode]*72
    tokens_yr = tps*util*365*86400
    silicon   = rack_price*annuity(wacc, amort)
    facility  = FAC_CAPEX_W[fac]*RACK_KW*1e3*annuity(wacc, FAC_LIFE)
    fac_opex  = FAC_OPEX_KW*RACK_KW
    power     = RACK_KW*PUE*8760*TARIFF_HYPER
    cost_yr   = silicon + facility + fac_opex + power
    parts     = dict(silicon=silicon, facility=facility, fac_opex=fac_opex, power=power)
    return cost_yr/(tokens_yr/1e6), cost_yr, tokens_yr, parts

# ---------------- Whole-model batching amortization ---------------------------------------------
# Two different series, routinely conflated. The expert-only series counts routed-expert reads
# only; the whole-model series counts every byte a decode step reads, including the ~27 GB of
# attention, shared-expert and embedding weights read on EVERY step regardless of batch. The
# second is the one that belongs in a cost comparison, and it is roughly twice the first.
def amort_expert_only(B):
    return B*K_EXP/distinct_experts(B)

def amort_whole_model(B):
    return B*step_bytes_gb(1)/step_bytes_gb(B)

# The text prints the same series on rounded constants -- 27 GB of shared weights, 1.5 GB per
# expert, D(1) = 51 GB -- so that a reader can reproduce it by hand. Both are printed below;
# they agree to two significant figures, which is all the underlying estimates support.
SHARED_GB_ROUND = 27.0
EXPERT_GB_ROUND = 1.5

def step_bytes_round(B):
    return SHARED_GB_ROUND + EXPERT_GB_ROUND*distinct_experts(B)

def amort_whole_model_round(B):
    return B*step_bytes_round(1)/step_bytes_round(B)

# ---------------- Pretraining time ---------------------------------------------------------------
# t = 6 * N_active * T / (N_sockets * F_socket * MFU). The 6 is the standard forward-plus-backward
# FLOP coefficient per active parameter per token; it assumes no activation recomputation, which
# is exactly what the 2.3 TB/socket capacity buys.
SOCKET_PF_FP8 = 20e15
MFU_LPDDR     = 0.67

def pretrain_days(tokens, sockets=128, f=SOCKET_PF_FP8, mfu=MFU_LPDDR, n_active=ACTIVE_P):
    return 6*n_active*tokens/(sockets*f*mfu)/86400

if __name__=='__main__':
    print(f"per routed expert: {per_expert_gb:.2f} GB; non-expert per step: {nonexp_gb:.1f} GB; batch-1 step: {step_bytes_gb(1):.1f} GB")
    print(f"HBF capacity {HBF_CAP_GB} GB in {HBF_STACKS} gen-1 stacks; checkpoint {CHECKPOINT_TB*1000:.0f} GB; "
          f"headroom {HBF_CAP_GB-CHECKPOINT_TB*1000:.0f} GB "
          f"(2 stacks = 1,024 GB does NOT hold it; 3 stacks = 1,536 GB holds it with 136 GB spare)")
    print("\n--- Appliance decode throughput (uniform routing, 6.4 TB/s HBF) ---")
    for B in [1,2,3,4,6,8,16]:
        print(f" B={B:2d}: distinct experts {distinct_experts(B):6.1f}  step {step_bytes_gb(B):6.1f} GB  per-user {per_user_tps(B):5.1f} tok/s  aggregate {B*per_user_tps(B):6.1f}")
    B=4; agg = B*per_user_tps(B)
    kv_bw = B*per_user_tps(B)*128e3*KV_PER_TOKEN_FP8
    print(f"\n KV traffic at B=4, 128K ctx, FP8: {kv_bw/1e9:.0f} GB/s of {LPDDR_BW/1e9:.0f} GB/s LPDDR6X")
    print(f" KV+state footprint, 8 seqs @128K: {(8*128e3*KV_PER_TOKEN_FP8+8*KDA_STATE_PER_SEQ)/1e9:.1f} GB")
    prefill_128k = 128e3*ACTIVE_P*2/SOC_FP4_DENSE
    print(f" prefill 128K prompt at {SOC_FP4_DENSE/1e12:.0f} TFLOPS dense: {prefill_128k:.0f} s; 32K: {prefill_128k/4:.0f} s")
    print(f" other models at 6.4 TB/s: DeepSeek V4-Pro (24.5 GB/step) {HBF_BW/24.5e9:.0f} tok/s; GLM-5 (20 GB/step) {HBF_BW/20e9:.0f} tok/s")
    print(f"\n--- Appliance power: full {P_FULL:.0f} W (HBF {P_HBF_FULL:.0f}), idle {P_IDLE:.0f} W; energy {P_FULL/agg:.2f} J/token ---")

    print("\n--- BOM and price: the HBF stack price is the only variable ---")
    print(f" non-HBF bill of materials, all three cases: ${NONHBF_BOM:,.0f}; OEM margin {MARGIN:.0%}")
    for k in STACK_PRICE:
        bom,p = price(k)
        print(f" {k:11s} ${STACK_PRICE[k]:6,.0f}/stack  BOM ${bom:,.0f}  price ${p:,.1f}")
    print(f" per-GB check: bare 512 GB stack at $150-250 is $0.293-0.488/GB; a FINISHED 1 TB NVMe")
    print(f"               at $65-100 retail is $0.065-0.100/GB -- a 3-7x gap, so the SSD does not bound the stack.")

    def machine_cost_mo(p, mo_tokens, wacc=WACC, closet=True):
        """MACHINE cost per month: capital, maintenance, closet UPS, energy. No labour."""
        E_kwh = (mo_tokens*P_FULL/agg + P_IDLE*(720*3600 - mo_tokens/agg))/3.6e6
        pue = CLOSET_PUE if closet else 1.0
        cap = p*annuity(wacc, AMORT_YRS)/12 + (CLOSET_CAPEX*annuity(wacc, CLOSET_LIFE)/12 if closet else 0)
        return cap + p*MAINT_FRAC/12 + E_kwh*pue*TARIFF_COMM, E_kwh*pue

    def spare_cost_mo(p, wacc=WACC):
        """A redundant node held idle: capital, maintenance, idle power. N+1, not N+0."""
        E_kwh = P_IDLE*720/1000*CLOSET_PUE
        return p*annuity(wacc, AMORT_YRS)/12 + p*MAINT_FRAC/12 + E_kwh*TARIFF_COMM

    loads = [('50M/mo',50e6),('100M/mo',100e6),('300M/mo',300e6),('capacity',agg*30*86400)]
    print("\n--- Appliance MACHINE cost per M output tokens (8% WACC, closet PUE 1.3, $500 UPS, no labour) ---")
    for k in STACK_PRICE:
        _,p = price(k)
        row = []
        for label, mo in loads:
            c,_ = machine_cost_mo(p, mo)
            row.append(f"{label} ${c/(mo/1e6):.2f}/M")
        print(f" {k:11s} (${p:,.0f}): " + "  ".join(row))
    print(" (straight-line, no WACC, no closet loading, base price, for reference:)")
    _,pb = price('base')
    print("   " + "  ".join(f"{l} ${machine_cost_mo(pb,m,wacc=0.0,closet=False)[0]/(m/1e6):.2f}/M" for l,m in loads))

    print("\n--- Appliance as an OPERATED SERVICE: machine + operator-hours + N+1 spare ---")
    print(f"     operator time at ${OPERATOR_RATE:.0f}/hour loaded; one hour a month is "
          f"${OPERATOR_RATE/100:.2f}/M at 100M, ${OPERATOR_RATE/300:.2f}/M at 300M, ${OPERATOR_RATE/540:.2f}/M at capacity")
    for k in STACK_PRICE:
        _,p = price(k)
        print(f" {k} price ${p:,.0f}")
        for label, mo in [('100M/mo',100e6),('300M/mo',300e6),('capacity',agg*30*86400)]:
            mc,_ = machine_cost_mo(p, mo)
            cells = []
            for h in OPS_HOURS:
                c = mc + h*OPERATOR_RATE
                cells.append(f"{h}h ${c/(mo/1e6):.2f}")
            sp = spare_cost_mo(p)
            for h in OPS_HOURS:
                c = mc + h*OPERATOR_RATE + sp
                cells.append(f"{h}h+N1 ${c/(mo/1e6):.2f}")
            print(f"   {label:9s} " + "  ".join(cells))
    print(" against same-year API list, $/M output: Kimi K3 $15.00, DeepSeek V4-Pro $3.96 peak /")
    print("   $1.98 off-peak, Qwen3.8-Max $6.00 -- an operated appliance at 100M/mo beats the cheapest")
    print("   Chinese list price only at 0-1 operator-hours, and the cloud can adopt cheap memory too.")
    print(" the crossover test: rack interactive parity 6-yr is $0.90/M.")
    _,po = price('optimistic')
    mc,_ = machine_cost_mo(po, 300e6)
    print(f"   optimistic price, 300M/mo, machine only ${mc/300:.2f}/M; +1 operator-hour ${(mc+100)/300:.2f}/M"
          f" -> {'ABOVE' if (mc+100)/300 > 0.90 else 'below'} $0.90")

    print("\n--- Rubin VR200 NVL72: fully loaded operator cost, per rack-year and per M tokens ---")
    for mode in TPS_PER_GPU:
        for am in (4,6):
            c,cy,ty,parts = central_cost_per_M(mode, am)
            print(f" {mode:38s} {am}-yr @8%: ${cy/1e6:.2f}M/yr [silicon {parts['silicon']/1e6:.2f} facility {parts['facility']/1e6:.2f} fac-opex {parts['fac_opex']/1e6:.2f} power {parts['power']/1e6:.2f}], {ty/1e12:.2f}T tok/yr -> ${c:.2f}/M")
    print(" facility share of fully loaded rack cost (4-yr):", end=' ')
    c,cy,ty,parts = central_cost_per_M('interactive parity (~50 tok/s/user)', 4)
    print(f"{100*(parts['facility']+parts['fac_opex'])/cy:.0f}%  (silicon {100*parts['silicon']/cy:.0f}%, power {100*parts['power']/cy:.0f}%)")
    print(" everything-but-silicon add-on per rack: capex ${:,.0f} once; ${:,.0f}/yr opex+power".format(FAC_CAPEX_W['P50']*RACK_KW*1e3, parts['fac_opex']+parts['power']))
    print(" straight-line, no WACC, for reference:", end=' ')
    for am in (4,6):
        c,cy,ty,parts = central_cost_per_M('interactive parity (~50 tok/s/user)', am, wacc=0.0)
        print(f"{am}-yr ${c:.2f}/M ", end='')
    print()
    print("\n--- Rack sensitivity: facility P10/P50/P90 and utilization (interactive parity, 4-yr @8%) ---")
    for fac in ('P10','P50','P90'):
        row = []
        for u in (0.60, 0.40, 0.30):
            c,cy,ty,parts = central_cost_per_M('interactive parity (~50 tok/s/user)', 4, util=u, fac=fac)
            row.append(f"util {u:.0%}: ${c:.2f}/M")
        print(f" facility {fac} (${FAC_CAPEX_W[fac]}/W): " + "  ".join(row))
    print(" the same at 6-yr silicon life:", end=' ')
    for u in (0.60, 0.40, 0.30):
        c,_,_,_ = central_cost_per_M('interactive parity (~50 tok/s/user)', 6, util=u)
        print(f"util {u:.0%}: ${c:.2f}/M ", end='')
    print()
    print("\n--- Rack at enterprise retail ($10M through an OEM, warranty and support) ---")
    for am in (4,6):
        for u in (0.60,0.40,0.30):
            c,cy,ty,parts = central_cost_per_M('interactive parity (~50 tok/s/user)', am, util=u, rack_price=RACK_PRICE_RETAIL)
            print(f" parity {am}-yr util {u:.0%}: ${c:.2f}/M ", end='')
        print()
    c,cy,ty,parts = central_cost_per_M('throughput (~25 tok/s/user)', 4, rack_price=RACK_PRICE_RETAIL)
    c6,_,_,_ = central_cost_per_M('throughput (~25 tok/s/user)', 6, rack_price=RACK_PRICE_RETAIL)
    print(f" throughput 4-yr ${c:.2f}/M, 6-yr ${c6:.2f}/M; per rack-year at 4-yr ${cy/1e6:.2f}M")
    print("\n--- Reconciliation with wholesale colocation rent (NoVA 10 MW+, $155-185/kW/mo ex-power, CBRE H2 2025) ---")
    c,cy,ty,parts = central_cost_per_M('interactive parity (~50 tok/s/user)', 4)
    bottom_up = (parts['facility']+parts['fac_opex'])/(RACK_KW*12)
    print(f" bottom-up facility annuity + opex = ${bottom_up:.0f}/kW-mo before landlord margin; colo asking rent $155-185/kW-mo")

    print("\n--- Batching amortization: expert-only against whole-model weight reads ---")
    print(f" D(1) = {step_bytes_gb(1):.1f} GB; shared weights read every step = {nonexp_gb:.1f} GB")
    for B in (8,128,512):
        print(f" B={B:3d}: D(B) {step_bytes_gb(B):7.1f} GB  expert-only {amort_expert_only(B):5.2f}x  whole-model {amort_whole_model(B):5.2f}x"
              f"  dense/sparse ratio {B/amort_whole_model(B):5.1f}x (expert-only reading: {B/amort_expert_only(B):5.1f}x)")
    print(f" on the rounded constants the text prints (27 GB shared, 1.5 GB/expert, D(1) = {step_bytes_round(1):.0f} GB):")
    for B in (8,128,512):
        print(f" B={B:3d}: D(B) {step_bytes_round(B):7.1f} GB  whole-model {amort_whole_model_round(B):5.2f}x"
              f"  dense/sparse ratio {B/amort_whole_model_round(B):5.1f}x")

    print("\n--- Pretraining time, 104B active, 20 PF(FP8) per socket, 67% MFU (before restarts) ---")
    for sockets in (128, 256):
        cells = [f"{t/1e12:.0f}T: {pretrain_days(t, sockets):.1f} d" for t in (15e12, 30e12, 60e12)]
        print(f" {sockets:3d} sockets ({sockets//2} dual-socket nodes): " + "  ".join(cells))

    print("\n--- API list prices, $/M output ---")
    api = {'Claude Opus 5 (AA 63)':25, 'GPT-5.6 Sol (AA 61)':30, 'Grok 4.6 (AA 61)':6,
           'Gemini 3.1 Pro':12, 'Kimi K3 API (AA 60)':15, 'Qwen3.8-Max':6,
           'DeepSeek V4-Pro (peak/off-peak)':(3.96,1.98)}
    for k,v in api.items(): print(f" {k:32s} {v}")
