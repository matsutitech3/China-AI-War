# Changelog

*How China Will Win the AI War: The Convergence Strategy* is a living book. Each release carries a **currency date** which is defined to be the date of the edition itself: every factual claim in the stable chapters is current as of the date on the title page, and anything learned after it belongs to the next release. Both editions — the full book and the condensed companion — are built from the same source tree and always carry the same version stamp and the same date.

This file records what changed at each release. Entries are newest first. Section and chapter numbers are those of the release being described.

---

## v0.23 — 9 September 2026

**Full edition 390 pages, five parts, 29 chapters · Condensed edition 56 pages · 778 bibliography entries (30 new)**

A release built from three claims that were checked before they were written, two of which did not survive the check in the form they arrived. Each is recorded here because the corrections are part of the record.

### New: Chapter 6, "Telecommunications: The Network War, in Lesser Detail"

A fourth Part I precedent, shorter than the three before it and different in kind — a network rather than a commodity. The measured record: Huawei from a fifth of the Chinese switch market (1996) to parity with Ericsson (2011); global telecom-equipment share 27.7% (2018) → 31% (1H2020) → **31% again in 1H2025**, 40% outside North America; the credit weapon — a China Development Bank facility for Huawei's customers of $10bn (2004) raised to **$30bn (December 2009)**, roughly $10bn drawn by 2013, the *Wall Street Journal*'s reconstruction of up to $75bn of state support, and a ~30% price undercut *where the credit was* (only slightly lower in Europe; ~25% higher at home); rural-first entry, then Africa, Asia and Latin America, then Europe; standards captured from inside 3GPP; and the bans — which removed share only in the Five Eyes, the Nordics and Japan, left European 5G share flat at ~32% from 2022 to 2024, and turned Britain not by a security finding but by the May 2020 *foundry* rule, a semiconductor chokepoint. The chapter ends on the disanalogy, stated plainly: AI has no credit line, no surplus capacity, and an artifact — open weights — that diffuses better than a switch and locks in nothing.

### The export offer, as it actually exists (Chapter 22, new section)

The claim arrived as "China is signing sovereign-AI infrastructure pacts with non-aligned nations the way Huawei built telecom networks." The record at the currency date: **WAICO** (founded 16 July 2026, 29 signatories, member dues, three ratifications to enter into force) and the two policy texts before it contain **no compute, financing, datacentre or open-weights commitment**; **Egypt** is a Huawei Ascend bid (~2,000 chips), unsigned, with a US counter-offer being assembled and no agreement from Xi's Cairo visit; **Malaysia** is a 910C evaluation, unsigned, under a US trade-pact constraint; **Brazil** is the one contract — R$1.3bn to Huawei/iFlytek, Brazil-financed, half the programme expected to go to NVIDIA; Kazakhstan and Pakistan are memoranda. **No Ascend export has been confirmed anywhere. No sovereign credit facility for AI has surfaced.** The US "American AI Exports" programme has 78 proposals and zero designations. Neither offer has been delivered anywhere. And capacity runs the other way: DeepSeek's reported ≥160,000-unit Ascend 950DT order may take a year to fill, and Beijing's reported ≥80% domestic-silicon mandate pulls chips home. The section prints the counter — intent precedes capacity in every precedent campaign, and Egypt is the live test — and adds a forecast-register row on the first confirmed Ascend export (40% [25%], end-2027).

### The toll road (Chapter 10, new section)

The claim arrived as "a profit-sharing proposal to host Chinese models on US hyperscalers, mitigating shutdown risk." The primary is a Reuters exclusive (26 August, three anonymous sources): **Moonshot is in early talks with Microsoft, Amazon and Google seeking up to 30% of Kimi K3 service revenue** — *revenue*-sharing, a lab-to-cloud negotiation, unsigned. What forces the talks is **K3's licence clause** obliging any model-as-a-service operator above $20M to contract with Moonshot — the reason K3, unlike K2.5, is not on Bedrock — and Alibaba is copying it. Against what exists: the hyperscalers already serve DeepSeek, Qwen, GLM and Kimi K2.5 "sold by AWS" with no disclosed payment to any lab. The section rejects the hedge reading on the evidence: no source attributes that motive, and the only serious analysis argues "with revenue comes regulability" — a contract makes a US restriction easier to apply, not harder. If there is a shutdown the toll road hedges against it is the Chinese one, and that is marked as the book's inference.

### The small-model argument and the benchmark re-basing (Chapter 10)

The claim arrived as "GLM-5.4-Flash, trained exclusively on Chinese chips." **There is no GLM-5.4-Flash** — Z.ai's own release notes, its Hugging Face organisation and every tracker show GLM-5.3-Flash (26 August) as the newest release. **The chip claim is a serving claim**: Zhipu's Chinese documentation says first-time *serving* of large-scale traffic on a domestic cluster, and no training-hardware statement exists for the model. The June "GLM-5 family trained on ~100k Ascend 910B" claim, which the book had carried as "unaudited," turns out to have **no locatable primary** — it circulates through trade press without a source, and Huawei's own announcement describes post-release inference adaptation. It is regraded [A/C] throughout both editions.

What does hold: on independent v4.3 sub-scores GLM-5.3-Flash is the **cheapest point on the price–agentic-coding frontier** — Terminal-Bench v4.0 at 33% against 12% for its price-tier peers — carrying ~12T tokens a month on OpenRouter alongside GPT-5.6 Luna and DeepSeek V4 Flash, while the closed flagship carries "the low billions." New subsection on **the barbell**: open weights at 36% of Vercel's July tokens on 8.6% of spend (62% on one day in August), the volume tier a sparse-mixture tier of 13–49B active parameters, and the top four laboratories still taking 95% of spend — volume moves to the open sparse tier, spend stays in the closed frontier, and spend concentration is the evidence the capability tier still commands a rent.

**Artificial Analysis re-based its index twice in one week (v4.2 on 4 September, v4.3 on 7 September).** Every index score in both editions now carries its version. On v4.3 the best closed models score 53, GLM-5.3 45 and GLM-5.3-Flash 42; the gap from best closed to best Chinese open is eight points, not three.

### September 2026 developments absorbed

DeepSeek's reported 160,000-unit Ascend 950DT inference order (inference only; training stays on NVIDIA) — the served-not-trained partition at the leading laboratory's scale (Chapter 12). The reported Commerce draft rule on remote access to NVIDIA compute in third countries (Chapter 12). Moonshot's confidential Hong Kong filing (Chapter 21). Today's NSA/FBI/CISA advisory naming six Chinese laboratories for distillation via cloud providers and aggregators — an allegation, not an adjudication (Chapter 18). MOFCOM's July consultations on curbing overseas access to the most advanced models, nothing decided (Chapter 10). WAICO's structure and absences (Chapter 20).

### Corrections applied

DeepSeek's funding round was misrecorded as "nearing $7.4bn at a $74bn valuation"; it closed in **June 2026 at $7.4bn above $50bn, with the state Big Fund as sole voting holder**. Thirteen verification findings fixed, including two appendix rows and two bibliography entries still carrying the Ascend training claim as primary; a stale launch-week index entry; date arithmetic left over from the previous currency date; three surviving edition-history phrases; a chapter count; a `\datafreeze` macro that swallowed the following space in eleven places; the Egypt bid described as the "first Ascend export attempt" when Malaysia's retracted 2025 announcement and the Brazil contract precede it; and a Moonshot revenue figure attributed to a confidential filing that cannot carry it.

### Condensed edition

The telecom precedent added to the precedents chapter; the barbell, the toll road, the re-based index and the fourth chip-claim qualification in the elements chapter; a new "export offer, as it exists" section with a table in the world chapter; the CISA advisory, the Brazil template and a forecast-register row. All `[full edition, Ch. n]` pointers shifted for the new Chapter 6. 56 pages.

---

## v0.22.1 — 1 September 2026

A correction of provenance. The departure recorded in Chapter 16 was described as an executive who "came from Meta and Google," which invited the common garbling that the "head of data centers" title travelled with him. It did not. That title was OpenAI's alone: at Meta he spent close to five years as a **distinguished engineer**, and before that nearly twelve years at Google on data-centre infrastructure and IT hardware research. Both editions and the bibliography entry now state this, and the full edition draws the consequence — the person OpenAI recruited to build its data centres was an infrastructure engineer of seventeen years' standing at the two firms that had built the largest ones, and OpenAI kept him sixteen months.

---

## v0.22 — 1 September 2026

**Full edition 368 pages, five parts, 28 chapters · Condensed edition 53 pages · 748 bibliography entries (30 new)**

A structural release. The book is reorganized from three parts into five, two chapters are added, and the Mirror chapter of v0.21 grows by about 58% on new primary evidence.

### Restructured into five parts

- **Part III — The Consequences** (Ch 17–22) now ends at "Strategies for the Rest."
- **Part IV — AI for Science: The Largest Prize** (NEW, Ch 23–26): the prize chapter, the new China chapter, the sizing chapter and the consortium chapter, which previously sat at the end of Part III and were read as an appendix to the consequences rather than as the argument they are.
- **Part V — Synthesis and Summary** (NEW, Ch 27–28): the convergence argument, then the whole book in short form.

### New: Chapter 24, "China's Scientific Machine: AI for Science as Industrial Policy"

The book argued that AI for science is the largest prize on the table and never set out how China is organized for it. This chapter does, and reads the policy record precisely rather than enthusiastically:

- **"AI+ science and technology" is the first of six key actions** in the State Council's "AI+" Opinions (Guofa [2025] No. 11) — ahead of industry, consumption, welfare, governance and cooperation — and its third science sub-clause chains AI-driven research to "engineering realisation and product landing," which is why the chapter is titled industrial policy. But the document's numeric targets are **diffusion targets; it sets no numeric target for science**.
- **The correction that matters**: the Party's 15th Five-Year Plan *Recommendations* contain "use AI to lead a transformation of the scientific research paradigm" — and **that phrase does not survive into the state Outline adopted in March 2026**, where AI appears under compute and data while basic research appears without AI. Anyone claiming the Plan makes AI4S a central pillar of the state programme is reading the Party document.
- **Output measured by the European Commission rather than by China**: its own bibliometric study finds China overtook both the US and the EU in AI-assisted scientific output from 2016, with the window ending in 2022 and output not being discovery.
- **The models are open, and the licence is the point**: Intern-S1 (241B, 2.5T scientific tokens, Apache 2.0); ByteDance's Protenix (Apache 2.0) claiming the first fully open-source model to beat AlphaFold3 at matched cutoff, scale and budget — the open-weight ratchet has reached structural biology, from a Chinese laboratory; and DeepModeling/DP Technology, among the most genuinely open scientific-AI ecosystems anywhere. Counter-observation: the newest and most capable platform has no stated open-source release and is access-by-invitation, so the openness may be a phase rather than a principle.
- **The state's top science prize went to the machine**, not to a discovery made on it: Pengcheng Cloudbrain, the first fully domestic large-scale intelligent computing system, took the National Science and Technology Progress Award First Prize.

### New: Chapter 28, "The Argument in Summary"

The book in short form, with the one thing the preceding chapters withhold: a single statement of where the balance of evidence sits. The question restated (not who builds the better model, but where the rent lands when intelligence becomes cheap), the answer in three parts, a table of the four propositions with their current status, eight observations that would change the answer, an instruction per actor class, and four disclaimers about what the book is *not* claiming.

### Chapter 16, "The Mirror," expanded on new evidence

- **NVIDIA is buying the open-model supply chain, not merely publishing weights.** The **~$7bn Poolside transaction** — $6bn for a non-exclusive licence to its "Model Factory" training platform, $1bn of equity, and **109 researchers hired to work on Nemotron** — and the **reported, unconfirmed ~$12.9bn Hugging Face acquisition**. Taken with Nemotron, that is the factory, the staff and (if the report is right) the warehouse. The chapter argues both readings: this is how a complement gets reliably supplied, and it concentrates the open layer under one balance sheet. A commons whose factory and distribution are owned by the vendor of the complement is a different object from a commons.
- **The structured-acquisition pattern**: Groq (~$20bn), Enfabrica (~$900m) and Poolside (~$7bn) — roughly $27bn in nine months, each structured so the target stays nominally independent and outside merger review. A Senate letter of March 2026 says NVIDIA "effectively acquired Groq in all but name." No enforcement action at the currency date — and an equity acquisition of Hugging Face *would* require review, which is why the report matters more than its price.
- **Jalapeño as a direct challenge, with the sentence that constrains how it can be read.** First results claim 1.5–1.9× work per watt and 1.7–3.6× lower latency — vendor-run, against Blackwell-class parts, with an HBM4-versus-HBM3E generation gap SemiAnalysis calls "incomplete and unfair," and **the part was not deployed at the currency date**. From the same OpenAI post: "We will continue to widely deploy accelerators from NVIDIA and other partners." Neither OpenAI's nor Broadcom's announcement names NVIDIA.
- **A correction to a widely circulated claim.** It was **OpenAI's own Head of Data Centers** who left OpenAI in August 2026; OpenAI's infrastructure lead was recruited from **Intel**; NVIDIA's data-centre leadership is intact; and the senior technical flow in 2026 ran *toward* NVIDIA.
- **The quarter as the filings state it.** "Gaming" has ceased to be a reported segment (folded into a new Edge Computing line); Data Center is split into Hyperscale (+102%) and AI Clouds, Industrial & Enterprise (+138%), with the faster-growing half being the one that is *not* the hyperscalers building their own silicon; ~70% revenue growth guided for fiscal 2028 against a ~44% consensus, on the call and not in the press release; and the equity investment in OpenAI fell from $100bn to $30bn while the compute commitment rose to ~12 GW through 2030.

### Consequence chapters expanded

Chapter 20 prices a new exposure class the book had not priced — guarantees and residual values — as **wrong-way risk**, with the SEC's July 2026 structured-finance position and its market-structure consequence. Chapter 21 rewrites the buyer's decision problem around **two commons rather than one**, and gives the new instruction to audit the *provenance* of the openness, not only the licence. Chapter 22 states the sharpest policy finding in the book: an export-control regime and an open-weight corporate strategy are aimed at the same object from opposite sides, and a denial policy contingent on the conduct of firms the government does not control is not a strategy.

### Corrections applied

A verification pass produced eleven confirmed defects, all fixed: the Preface roadmap still described a three-part book; a 117% data-centre growth rate was attributed to total revenue; the condensed edition presented total-company guidance as data-centre guidance and asserted a guided data-centre run rate that does not exist; a superseded quarter ($81.6bn) survived in the condensed trade chapter alongside a larger data-centre figure; two claims were over-graded [V] when the full edition grades them [A] and [P/A]; date arithmetic was off by one throughout after the currency date moved; the condensed edition silently resolved a disputed announcement date; a duplicate bibliography entry printed the same source twice under two numbers; and researcher counts read as compute requirements in the condensed sizing summary.

### Condensed edition

Two new chapters mirroring the above ("China's Scientific Machine," "The Argument in Summary"), the Mirror and trade chapters updated, and roughly 17 kB of body cut to pay for them — chiefly restatement between the elements, mirror, convergence and summary chapters. 53 pages.

---

## v0.21 — 31 August 2026

**Full edition 335 pages · Condensed edition 50 pages · 726 bibliography entries (52 new)**

The largest structural change since the condensed edition was introduced. This release is a restructure rather than an addition: the book's central claim has been that China runs a commoditization playbook against Western rent layers, and the evidence of mid-2026 required that claim to be generalized rather than merely extended.

### New: Chapter 16, "The Mirror: The West Runs the Playbook Against Itself"

A new chapter closing Part II, reporting that over the course of 2026 the largest Western firms converged on the same method the book attributes to Beijing. Each now commoditizes, deliberately and at its own near-term expense, a layer it does not own in order to defend the layer it does.

- **NVIDIA commoditizes the model and underwrites the buildout.** Nemotron 3 and 3.5 Lightning released with weights *and* training datasets *and* reinforcement-learning libraries (OpenMDW-1.1); a pretraining collection above ten trillion tokens; cuTile and the CUDA Tile IR open-sourced under Apache 2.0; Nemotron 3 Ultra sixth by weekly tokens on the largest neutral router. The rationale is on the record twice — Huang's "nearly all open models run on NVIDIA … the CUDA ecosystem is literally everywhere," and NVIDIA's own director arguing that durable value accrues to data rather than weights. On the financing side: the $105B capped residual value guarantee on the Ohio leases, $108.5B maximum gross guarantee exposure, $279B supply commitments, ~$95.6B of equity securities, the $6.3B CoreWeave residual purchase obligation, and $500B of financing memoranda with six asset managers — preceded twelve days earlier by the SEC's structured-finance position taking data-centre securitizations outside Regulation AB and the 5% risk-retention requirement.
- **The laboratories and hyperscalers commoditize the silicon.** Jalapeño with Broadcom under a 10 GW term sheet; TPU 8t/8i and Google's decision to deliver TPUs into customers' own datacentres; Maia 200's "30% better performance per dollar" framing with NVIDIA unmentioned; MTIA; more than a million Trainium processors deployed; Broadcom AI semiconductor revenue at $10.8B (+143%) guided above $16B. And the fabric: the scale-up domain is now built from merchant Ethernet almost everywhere.
- **SpaceX commoditizes the fab.** Terafab, graded as intent rather than capacity: the announced figures have moved three times, no node or timeline was restated in the August confirmation, and the project went undiscussed on SpaceX's first earnings call the same week.
- **The asymmetry that survives**, argued in both directions. Commoditization is not losing — the scarce layers are still mostly Western-held, and the price inversion of 30 July shows the incumbent pricing *underneath* the commodity and gaining share. Against that: every Western move commoditizes a layer another *Western* firm was earning rent in, and the layers being commoditized are disproportionately the ones China is behind in. An export-control regime and an open-weight corporate strategy are aimed at the same object from opposite sides.
- **Counter-evidence printed in full**: the 27 August pause of parts of the revenue-share programme over internal antitrust concerns; the retrenchment from $100B to $30B and from $250B to $105B; the Ohio guarantee's termination on an OpenAI credit-rating event with full indemnification; and — decisively — AWS committing to two million additional NVIDIA GPUs while Trainium4 adopts NVLink Fusion and NVIDIA custom HBM. The honest reading is that the incumbent is absorbing the custom-silicon wave rather than being displaced by it.

### New: Appendix C, "The Hot Chips 2026 Ledger"

The evidence base for the above, drawn from the 31 technical presentations at Hot Chips 2026 (Stanford, 23–25 August). Tables of the datacentre CPUs and the accelerators as presented; the four schools of thought for beating the GPU; the bifurcation of FP64 into a product-line decision; what the conference says about openness; and a methodological warning that disclosure has collapsed unevenly and the parts with the strongest competitive position disclose least — so peak-FLOPS tables are now partly unbuildable and the only universally available axes are memory capacity, memory bandwidth, fabric bandwidth and scale-up domain size.

### Element chapters, substantially revised

- **The Model (Ch. 9).** GLM-5.3 (weights released 28 August under a custom licence requiring security review of large model-as-a-service operators) and **GLM-5.3-Flash** — MIT, 320B total / 18B active, natively multimodal, fourth of 111 on the independent capability index at $0.09 per task against the flagship's $1.40, and small enough at three-bit quantization (120 GB, 81.6% top-1) to run on a single 128 GB workstation-class machine. The domestic-silicon claim attached to it is recorded with its three load-bearing qualifications: it is about **serving, not training**; **no chipmaker is named**; and **it is not a first**. New section on the **price inversion**: the 30 July cut was to Luna, the *cheapest* tier, taking it below the list price of the frontier-scale Chinese open-weight models, with usage rising to 13.8× and roughly three-quarters of the gain taken from competitors — while DeepSeek *raised* prices by as much as 1,100% on 13 August, mid-cascade. No one-directional price-war account survives that sequence.
- **The Compute (Ch. 11).** NVIDIA's published requirements for a RISC-V CPU to host CUDA, and the finding that almost none of them are about the instruction set — with the sting that coherent unified memory still requires NVLink-C2C soft IP speaking CHI, an Arm-originated protocol, under a partner-only specification. The rent moved from the ISA to the coherent interconnect. Four competing matrix-extension proposals and no ratified one. Canonical's 55.1% package pass rate against 92.3% on amd64. SiFive BigSky, the first rackable enterprise RISC-V server — specified as a CUDA head node.
- **The Semiconductor (Ch. 12).** The 2026 memory wall is priced, not clocked: spot DRAM up 7.1× and NAND up 6.9× from the mid-2025 trough, combined supplier revenue from ~$15B to ~$180B a quarter, memory from 52% to 63% of AI-chip component spend. New section: **"HBM4 stopped being a specification"** — a 1.5× spread in per-stack bandwidth within one JEDEC generation, so a bill of materials specifying "HBM4" does not specify a part. The base die is now a 4 nm foundry logic die, custom HBM is explicitly not JEDEC-standardized, and the chapter's "three to four years behind" finding is restated against two clocks rather than one.

### Corrections applied

Two full adversarial review passes were run and every finding applied. The substantive corrections:

- The capacity-floor result in Chapter 11 rested on 288 GB as a "physical limit of current HBM4 stacks." That is a packaging convention, not a JEDEC ceiling — AMD's MI455X ships 432 GB. The floor is re-derived (roughly 136 accelerators at eight stacks, 91 at twelve) and now depends on which vendor's HBM4 was bought, which is the point of the new HBM4 section.
- The 30 July price cut was dated 31 July in three places and described as a cut to the "mainline" product. Corrected throughout: 30 July, cheapest tier, flagship held.
- The custom-ASIC revenue ratio was stated as 15–18%. Re-derived from the two primary filings as 11–15%, with the range explicitly attributed to which quarter and which basis is annualized.
- The RISC-V matrix-extension window was given as February 2026 – April 2027. The correct span is August 2026 – April 2027, with IME's 27 August target falling four days before this edition's currency date and no ratification announcement appearing by then.
- China's March 2025 eight-agency RISC-V guidance is now stated as *reported in preparation and never shown to have been formally issued*, graded [A], rather than as promulgated policy.
- The Zhipu Ascend-training claims are dated correctly (January and June 2026) and marked unaudited wherever they appear.
- The dashboard's own row count, the Kimi K3 licence threshold, the enterprise open-weight spend series endpoints, the HBM4 bandwidth multiple, and several cross-reference types (`Section` vs `Chapter` vs `Appendix`) were corrected.
- Relative dates that had gone stale ("nine days before this edition", "in the week before this edition closed", "this week") replaced with absolute ones.

### Register

Two falsification rows added to the forecast register, both resolving by end-2027: whether merchant-GPU revenue growth decelerates while custom-ASIC revenue holds its guided trajectory (the pincer reading), and whether custom accelerators keep converging onto NVIDIA's interconnect and memory (the absorption reading).

### Condensed edition

New Chapter 5, "The Mirror," mirroring the full chapter at condensed scale with its table, its counter-evidence and its licences intact. The elements chapter carries the GLM-5.3 material, the price inversion and the Hot Chips findings. Roughly 8% of the body was cut to make room — chiefly restatement between the elements, strategy and convergence chapters, a chronology table whose content is carried elsewhere, and a probability table duplicating the appendix register. The generated reference list now prints each source's identifying detail and its **full URL** in three columns; the analytical annotation on each source lives in the full edition. All `[full edition, Ch. n]` pointers renumbered for the new Chapter 16 and Appendix C.

### Build

Both editions build clean on a three-pass `pdflatex`: zero undefined references, zero undefined citations, zero duplicate labels. `make`, `make check` and `make check-condensed` unchanged.

---

## v0.20.2 — 18 August 2026

The strategy-assembly chapter moves from the head of Part III to the head of Part II (Chapter 8, immediately before "The Model"), reframed as a map drawn before the territory. Part II and III chapters renumber accordingly. The condensed edition's matching chapter moves likewise, and its reference list now prints every URL in full rather than abbreviating links, so the document stands alone. 49 pages.

## v0.20.1 — 18 August 2026

New chapter, "The Strategy Assembled: Part II Read Through Part I," placing each element on the playbook with a moves-by-element table and scoring the campaign against the six steps. Two adversarial review passes applied: statuses aligned with the source chapters' grades, Step 3 carrying the book's own overbuild self-critique, Step 5 printing both readings of the July price cut. The condensed edition gains a matching chapter, a front-matter glossary, a rent-migration table, a separate "Strategies for the Rest" chapter, and ~140 selective references; 25 review findings applied, including an invented licence threshold removed and an inverted battery cost-penalty corrected.

## v0.20 — 16 August 2026

**The condensed edition is introduced** — a short-form companion built from the same source tree under the same version stamp. Part I's precedent campaigns are summarized in one chapter and the weight shifted to the overall strategy and its international consequences; the forecast register and quarterly dashboard are reproduced in full. `make` now builds both editions; CI builds, checks and attaches both PDFs.

## v0.19.1 — 16 August 2026

Xiaohongshu's dots3-note Preview and TEMPO long-horizon RL; Xiaomi MiMo-V2.5; Vercel AI Gateway production data (open-weight models 29% of enterprise tokens on under 4% of spend); MacroPolo talent-location shift. Figures circulating online as "Tracker 3.0" flagged as not the Institute's and not used.

## v0.19 — 15 August 2026

New Appendix B, a ~15-page technical dossier on High Bandwidth Flash with ~50 new references: lineage, the announcement record, the OCP specification and the quantities it does not publish, power and energy physics, endurance, cost structure with an explicit reconciliation against the vendors' own framing, the bull and bear cases item by item, the competitive landscape, the China/YMTC angle, and the research literature.

## v0.18.3 — 15 August 2026

The rack and the appliance are now priced at the same point in the chain. The $7.8M VR200 NVL72 figure is identified as a costed component list at cloud-provider prices with NVIDIA's margin already inside, not cost of goods; because what buyers actually pay disperses widely, the model runs the rack at both $7.8M (hyperscaler) and $10M (enterprise retail with support).

## v0.18.2 — 14 August 2026

The rack side of the head-to-head now carries its building explicitly: facility capex per watt of IT load, a fifteen-year facility life against four-to-six for silicon, facility operations, an 8% cost of capital charged to both sides, and a utilization sensitivity. The railroad precedent added to the trade chapter — the network shrank because a distributed substitute took the traffic.

## v0.18.1 — 14 August 2026

The appliance cost model re-anchored to pre-surge finished-system pricing rather than post-surge component pricing; base-case price falls from $6,900 to $5,000. Two appendix tables converted to `longtable` after being found to overflow their float and silently drop rows with no LaTeX warning.

## v0.18 — 14 August 2026

New section pricing a capacity-first appliance against a Rubin NVL72 rack from a published bill of materials and measured throughput, with the model script shipped in `models/`.

## v0.17.2 — 13 August 2026

The OpenAI executive departures reweighted against the base rate; softening language removed.

## v0.17.1 — 13 August 2026

Memory section corrected: HBF's non-volatility and refresh-power implications; JEDEC's LPDDR6 SOCAMM2 roadmap; ZAM restated as a capacity architecture. RIKEN investment disclosed.

## v0.17 — 13 August 2026

New section on the memory unlock, with the novel quantitative result that for ultra-sparse MoE the centralized batching advantage collapses to roughly 9× at batch 512 against 512× for a dense model — the architecture adopted under compute scarcity is the one that most erodes the centralized serving advantage. Counter-case stated at full strength.

## v0.16.2 — 12 August 2026

New section dismantling the claim that western Chinese capacity cannot serve inference, with the NDRC latency target read correctly and measured east–west figures against it. Voice and inline completion conceded at full strength.

## v0.16.1 — 12 August 2026

New section on the commodity turn: compute futures, energy-normalized indices, backwardated forward curves, and why the monopolist's utilization backstop stands as an undisclosed price floor under every spot print.

## v0.16 — 15 August 2026

New chapter, "The Harness: The Layer the Contest Moved To." Models are swappable; harnesses are programmed to. Agent-standards governance with no named Chinese members against the CAC's July initiative. The thesis narrowed to lock-in relocating to distribution, evaluation substrate and certification.

## v0.15 — 11 August 2026

Meta's return to open weights, with the ratchet analysis extended across the Pacific and both readings registered as a dated forecast. Qwen weight slippage documented and the licence forecast revised.

## v0.14 — 4 August 2026

First public release in this repository.

---

## Conventions

- **Evidence grades** used throughout the book: `[V]` verified, `[P]` primary, `[A]` analyst, `[M]` author-modeled, `[R]` roadmap, `[S]` scenario.
- **Propositions P1–P4** are the four load-bearing claims, stated, coupled and falsified separately.
- Resolved forecasts are recorded as resolved in the register rather than removed, including those that resolved against the book.
- Corrections are welcome and will be credited. See `README.md`.
