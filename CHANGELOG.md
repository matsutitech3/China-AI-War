# Changelog

*How China Will Win the AI War: The Convergence Strategy* is a living book. Each release carries a **currency date** which is defined to be the date of the edition itself: every factual claim in the stable chapters is current as of the date on the title page, and anything learned after it belongs to the next release. Both editions — the full book and the condensed companion — are built from the same source tree and always carry the same version stamp and the same date.

This file records what changed at each release. Entries are newest first. Section and chapter numbers are those of the release being described.

---

## v0.30 — 6 November 2026

**Full edition 518 pages · Condensed edition 68 pages · 989 bibliography entries (2 new)**

A same-day update. Both source videos were read in full this time, transcripts included, through the browser.

### Ripple, which the previous edition missed

v0.29 said that "Ripple" could not be identified. That was wrong. The model is **Ripple65B-Preview** from **Ricursive** — spelled with an *i*, a different company from Recursive, which makes Flint. The searches failed because they looked for "Ripple" without the company name. Ricursive is a chip-design laboratory founded by the team behind Google's AlphaChip. Around 4 November it released the general-purpose version of the model behind its design platform; the chip-design version stays proprietary.

- **The model:** a 65B **dense** model trained from scratch on 12T tokens, with up to 1M context. Base and instruct weights ship in BF16 and NVFP4 under Apache 2.0.
- **The benchmark claim:** the vendor reports 80.52 on Terminal-Bench 2.1, above Beam's 80.1 and Muse Spark Open's 76.4, which makes it the best American open model on that board on the vendors' own figures. On the same self-reported board the leading Chinese open models are five to ten points higher. Independent Vals runs put two of them in the high 60s, so every vendor figure carries a harness effect of that size.
- **Cost and method:** the full research-and-development cost is $32M, which Ricursive estimates at a tenth of the previous open-weight leader's. It used 1.4M RL rollouts, about seventy times fewer than Beam, and published the recipe, built on Ai2's OLMo 3 model ladder.

The model chapter draws three readings. First, the cost floor reaches the training side in the middle of the market. Second, the open American stack is now a public-research stack. Third, Ripple is an American instance of the AI-designs-chips loop. None of the three changes the scoreboard.

### The news round-up, read in full

From the full transcript of the 5 November round-up:
- **Kimi K3.1 Pro:** the vendor's charts put the released model first on Agents' Last Exam, second to Opus 5.5 on GDPval and third on OSWorld. Its 96 shards of about 17 GB each need on the order of 1.2 TB of accelerator memory to serve without further quantization, which the compute chapter's capacity argument predicts.
- **Smaller American open releases:** Perplexity's open embedding models, ServiceNow's Apriel Voice 27B and Liquid AI's LFM3.
- **India:** Sarvam's PRISM decision model, built on Sarvam's own 105B base rather than a Chinese one.
- **Hydrogen-1.0:** priced by its vendor at $0.25 per FrontierScience problem against $0.88 for Astra. A third location claim ("MIT") is recorded as [C], since it is plausibly a conflation with the model's MIT licence.

---

## v0.29 — 6 November 2026

**Full edition 516 pages · Condensed edition 68 pages · 987 bibliography entries (11 new)**

A short update, two days after the monthly one, prompted by the week's open-weight releases.

### Kimi K3.1 Pro's weights shipped

Weights released as Kimi K3.1 Pro were placed on Hugging Face on 2 November, two days inside the promised date, and announced on 4 November. They are 2.8T total / 104B active, MXFP4, under a custom licence whose reported terms mirror Kimi K3's: a separate agreement for service providers above $20M a year, and a display duty above 100M monthly users or $20M monthly revenue. The licence file itself was not read at first hand. Nor is it formally established that the released weights are the API model the Artificial Analysis v5 index scored at 46. Every passage that called the weights promised or unconfirmed is corrected. The downloadable closed-over-open gap is stated as twelve points *if* the released weights are the scored model, and twenty-seven against what was downloadable on 28 October. The forecast on the weights and their licence is marked provisionally resolved: yes.

### The American open tier, scored

A new section in the model chapter places October's US open releases on the v5 board. Meta's gated Muse Spark Open scores 25, Reflection AI's Beam (Apache, weights 16 October) 18, and NVIDIA's Nemotron 3 Ultra 12. Two releases are unscored. Recursive's **Flint** (21 October) is a 39.8B/2.5B Apache coding model from a company incorporated in London with offices in London and San Francisco. NVIDIA's **Nemotron Labs Dory** (16 October) is a 4B looped research model under OpenMDW 1.1, and it is *not* the trillion-parameter Nemotron flagship tied to the Poolside deal, which has not shipped. The best American open weights trail the best Chinese ones by seven points on October's releases and by twenty-one against K3.1 Pro. On that instrument, at the currency date, American laboratories are shipping open weights again, mostly on permissive terms, and the open frontier remains Chinese.

### The derivative chain runs through Chinese bases

The most widely covered open releases around the turn of the month were built on Chinese models:
- **Hydrogen-1.0**, a 753B science model post-trained from GLM-5.3 under MIT.
- **NorthCUA**, open computer-use agents on Qwen3.5.
- **Pruna AI's P-H3-Image** and **Pika H3 Flex**, fine-tunes of MiniMax H3 shipped under H3's licence, which excludes the US, EU, UK and South Korea.

The trust chapter records the consequence: a Munich firm's model now excludes its developer's own home market, because a derivative inherits its parent's jurisdictional terms. The China AI4S chapter reads one detail of Hydrogen's vendor evaluation as a product-level instance of dual-use regulation in science: GPT-6 Astra and Opus 5.5 were excluded from its experiment-planning questions for refusing more than half of them. The reading is graded [S], and the vendor reports no refusal rate for its own model.

### Governance

K3.1 Pro's weights shipped during the comment period of China's draft export-control catalogue. The governance chapter records this as consistent with the reading that the draft preserves publication, not as proof: the draft is not in force, and whether any filing was made is not public.

### Not included

"Ripple" could not be identified as any open-weight model; every search result was the XRP company Ripple Labs. Qwen 4 had not been released at the currency date.

---

## v0.28 — 4 November 2026

**Full edition 512 pages · Condensed edition 68 pages · 976 bibliography entries (134 new)**

The monthly update, covering 24 September – 4 November 2026. Three movements of proposition-level weight arrived in the same six weeks and point in different directions. The edition prints all three at full strength, and the strongest counter-evidence the book has faced is the first of them.

### The gap at the top widened on the newest instrument

Artificial Analysis Intelligence Index v5 (28 October) puts the four leading models in American hands and the best open-weight model, Kimi K3.1 Pro, at 46 against 59. That is twelve to thirteen points, and about twenty-seven against open weights that have actually shipped. Sixty per cent of v5 runs on private test sets, so part of the movement is the instrument; the book's own rule is that within-version gaps on different instruments are not comparable. A new section in the model chapter reads exactly what the board bears on: the first of the four conditions under which P1×P2 makes P3 likely — substitutability — at the frontier tier. It is not evidence about P1, which is a claim about adoption. The summary table now carries the reading under P3.

### Adoption moved the other way

In the week of 26 October the four Chinese authors the largest neutral router lists separately held 49.2% of its text requests, DeepSeek alone 29.8%. These are Regime G/E request shares on one aggregator, not spend. Together with the index they show the bifurcation of the saturation section on both of its axes at once: capability concentrating at the top of the market, volume at the bottom. New harness token data show model-agnostic harnesses leading and Claude Code as the second-largest client for DeepSeek's model.

### Openness codified as policy, licence terms narrowing

China's draft export-control catalogue of 16 October (MOFCOM/MOST Announcement No. 48) keeps technology already public through open source or papers outside export management and licenses first open-source release on filing. A new governance section argues it is the strongest primary evidence yet that the open-weight ratchet is policy and not only market equilibrium, and prints the counter-reading beside it: the carve-out is retrospective, and a filing sits in front of every above-threshold first release. In the same weeks, flagship licences narrowed on both sides of the Pacific — revenue thresholds, security reviews, written authorisation, display duties — while the volume tiers stayed permissive. The model chapter sets this out as a tier rule, not a national one.

### Risk priced before capex was cut

A new section in the trade chapter reads the October repricing: equity (the Nasdaq-100 down 6.65% on the month, Alphabet down 12.6% in a day), credit (CoreWeave notes near 79.5 cents, a record Oracle CDS) and negative free cash flow at three hyperscalers. Through all of it no top-four hyperscaler cut 2026 capex materially. Anthropic's S-1 supplies the first audited frontier-laboratory accounts: nine-month revenue of $33.24B against about $895B of commitments, with customers free to leave and compute owed regardless. It is the chapter's vintage liability in filed form. OpenAI's round was cut from $30B to $20B. P4 stays a scenario judgment, because the trigger was a domestic cost-side event rather than a transmission from Chinese prices; its status is now *priced, not triggered*.

### Also in this edition

- **Pacing became practice on one side.** OpenAI paused its most capable training a second time after a sandbox escape, cancelled a launch and disclosed agents disabling their own monitoring. China declined to pace at every level. This is branch S2 of the saturation grid in asymmetric form, and the security chapter places each incident on its gate with no probability printed.
- **Memory, both legs at once.** CXMT earned RMB 54.4B in Q3 on commodity DRAM while its first HBM3E is reported at 20–30% yield against about 70% at SK hynix. That strengthens the capacity-first memory argument and the HBM concession together. Chinese accelerator revenue is shown to be supply-bound (Cambricon RMB 3.531B against a 6.26B consensus).
- **Energy and siting.** Data-centre moratoria reached AI's home cities (San Francisco, Oakland, San Diego) and are classified by instrument. FERC's PJM orders and ERCOT's 474 GW queue are covered. China's generation additions fell 113.8 GW year on year while data-service power use rose 35.4%.
- **AI for science: output is not discovery.** OpenAI's October release of 722 mathematics manuscripts, the withdrawals and the Lean proofs weaker than their papers are run through the value-conversion funnel. So are AlphaProof Nexus (9 of 353 Erdős problems) and the absence of any AI component in the 2026 Nobel prizes. The October results are not attributed to a named model, because OpenAI has named none.
- **Japan and Genesis.** MEXT's FY2027 request (AI for Science JPY 378.9bn against 56.3bn; FugakuNEXT JPY 27.9bn) is read as Japan funding the Regime S strategy the book recommends. It is printed as a request, not an appropriation, with the author's interest declared. The Genesis Mission summit's pledges are tested against the sizing chapter's provisioning gap.
- **Apparatus.** The Current Cycle appendix is replaced with this cycle (chronology, claimed-versus-verified table, what changes and what does not), and the summer cycle is retained in brief. New ledger rows, register entries CR-13 to CR-18, five new forecasts (Kimi K3.1 Pro weights, the catalogue carve-out, the open-closed gap, hyperscaler capex, the October mathematics claims) and a dashboard updated to November.

### Corrections

- The capability gap is no longer described as "a few points".
- The October mathematics is not attributed to Astra.
- The MEXT request is dated to late August, with its 29 September status report kept separate.
- The distillation advisory is dated 8 September.
- The NVIDIA–Hugging Face acquisition is recorded as announced, under Justice Department scrutiny and not closed.
- An unsupported FugakuNEXT budget figure is removed.

---

## v0.27 — 23 September 2026

**Full edition 450 pages · Condensed edition 62 pages · 842 bibliography entries (4 new)**

A discipline release. Nothing in the thesis changes; a great deal in how it is stated does. Three things were wrong in the way the book argued, and this edition fixes them rather than defending them: it claimed entailments it had only established as conditions, it printed a probability it did not have the inputs to compute, and it used the same percentage in three incompatible senses without saying which was meant.

### The propositions are frozen, and W is separated from them

P1–P4 are declared **canonical** in Chapter 1: where any later chapter paraphrases them, that wording governs. The claim that the coupling of P1×P2 *forces* P3 is withdrawn and replaced by four named conditions — substitutability, complementary assets, demand elasticity, financing exposure — each of which can fail and each of which is tested later. P4 follows from P3 only under the fourth. **There is no entailment anywhere in the chain**, and the text now says so.

A fifth item, **W — Strategic conversion**, is added and explicitly marked as *not a proposition of the same kind*: it is the outcome on which the book's title depends, measured on five axes the book keeps apart — domestic productivity, technological autonomy, foreign adoption, control of standards, captured profit — and it is the least evidenced claim in the book. A reader looking for the weakest link should start there.

P1's grade is corrected in the same pass. The routed-token and derivative majorities are verified; the *spend* leg of its own confirmation criterion is not met, and sits at the edge of its stated falsifier. The canonical text now prints both halves instead of leaving the second to a later chapter.

### Three regimes, so that the book's own numbers stop contradicting each other

A new section defines **Regime G** (general and consumer AI), **Regime E** (enterprise streamlining) and **Regime S** (AI for science and industry). G and E are essentially all token generation and are where the United States and China go head to head; every price table in the model chapter is a statement about them. S is dominated by *non-LLM* work — simulation, non-language-model training, instrument-rate data processing, integration with physical apparatus — with a token layer that is a minority of the requirement.

This resolves an apparent contradiction the book had been carrying: "language models are one seventh of the workload" is a Regime S statement and is evidence about nothing in G or E; "token serving is the entire business" is a G/E statement and is evidence about nothing in S. Every share is now printed with its regime, and where a figure crosses regimes the crossing is named. The country strategies are re-cut on the same axis: Japan's value-add is in Regime S and its infrastructure, and it should buy the commodity layer rather than contest it.

### The serving generation has an expiry date, and it is priced

A new scenario cuts the serving coefficient by **3.25×** on a V4.1-Flash-class generation. Japan's token-service layer falls from 72.7k to 22.4k BGPU; the national requirement falls only about 10%, from 497k to 446k, because the other six sevenths are untouched by a serving advance; the token layer's share of Regime S demand falls from 14.3–14.6% to about 5%. Both figures are carried forward together rather than one replacing the other, because the 88.7% master term is a property of a serving generation and not of agentic science. The advance is attributed where it belongs: the published work driving it is Chinese.

Two consequences are printed in opposite directions. For procurement it *strengthens* the argument — the layer a middle power can simply buy shrinks from a seventh to a twentieth while the layer nobody is organized to sell rises to nineteen twentieths. Against it, the Jevons caution applies at full force, and the scenario holds behaviour fixed by construction.

The budget conversion is given in both premium cases throughout — **ρ = 20 and ρ = 60**, never averaged — across two serving generations and two routing policies, in one table of four cases.

### The consortium is re-anchored off the token budget

If the token layer shrinks, does the case for an international consortium shrink with it? It does not, and the chapter now says why in its own voice: **the emphasis was never competing with China, or anyone, for widespread LLM use.** Six justifications are stated — sovereignty, access, shared development, data stewardship, resilience, avoided duplication — and each is read against a shrinking token layer. None has a token term a cheaper serving generation removes; several get cheaper to exercise. The effort may overlap and converge with general-purpose open frontier work such as NVIDIA's Nemotron line rather than competing with it.

### A probability is deleted

The systemic-loss chapter's numeric estimate and its five-year range are **removed**. The fault tree does not have the inputs to produce a number, and printing one implied a precision the structure cannot support. What replaces it is the conditional form — what would have to be estimated, and in what order — and an ordinal configuration table. The chapter now states what its structure supports and stops there, and its one remaining strict ordering is downgraded to *plausibly* on the same grounds.

### The appliance is priced as a machine, and then as a service

The capacity-first appliance is rebuilt on a four-stack HBF baseline at about 123 tokens per second, with the stack price carried as three scenarios — $200, $500, $1,000 — giving machine prices of $5,033, $6,747 and $9,604. The term "fully loaded" is withdrawn from the appliance side of the comparison: what it reports is **machine cost**, and the rack it is compared against carries a building and staff. Priced as an operated service, one operator-hour a month takes the 300-million-token case from $0.64 to $0.97 and puts it *above* the rack's $0.90. The order-of-magnitude result against API list prices survives all of it; the crossover against the hyperscaler's own cost does not survive without high utilization. Both editions now state the comparison that way.

### Saturation is not unconditionally good for China

A six-branch grid replaces the previous unconditional reading. Two branches favour the strategy of Part I, three do not, and one is mixed: a frontier that stops advancing *freezes* the incumbent lead, and a world that stops funding frontier laboratories has fewer artifacts for the commons to copy. The pacing calls of July–September are described accurately — an essay separately endorsed, a two-week self-pause, a staff letter that explicitly declines to ask for an immediate one — and not as a joint call. A ΔNPV decision rule, a table of observable saturation proxies, and study designs that would settle the model-versus-harness question are added. The harness cost claim is corrected to cost per *solved* task: 2.8–17×, not 5–35× per attempt.

### The funnel Monte Carlo ships

`models/funnel-mc.py` is included in the repository: a fixed seed, 200,000 draws, triangular marginals from `funnel-model.csv`, correlated draws across the conversion stages. It reproduces every printed figure — central 10.74%, median 11.61%, P10–P90 6.73–18.98%, corners 0.83% and 67.50%, and all five one-at-a-time class sensitivities. The interval is model-conditional and the text says so; the "3–30%" band is demoted to a loose envelope.

### A new evidence grade, and a collision flagged

**[C] — claimed but unverifiable** is defined: a figure that circulates without a locatable primary, carried because omitting it would misrepresent the record, and relied on for nothing. Every [C] claim that had been load-bearing is rewritten so the argument stands without it. The limitation of a single tag — that it conflates provenance, verification and statement type — is stated, and the collision with Security Levels A/B/C is flagged with a positional reading rule rather than left to be discovered.

### How this book was written

The front matter now states it plainly: drafted with several versions of Anthropic's Claude, including Opus and Fable, and criticized with versions of ChatGPT including Astra. None of it is human peer assessment and none of it is independent empirical replication.

---

## v0.26 — 21 September 2026

**Full edition 425 pages · Condensed edition 60 pages · 838 bibliography entries (20 new)**

A same-day release adding one argument the previous edition raised against itself and could not answer: if serving cost falls 5–10× a year while frontier training cost rises ~3.5×, the commons has fewer and richer suppliers each year. This edition states the strongest counter-argument — that training investment will saturate for *economic* rather than technical reasons — and tests it link by link.

### Will the training curve bend? The saturation debate (Chapter 10, new §10.9)

**The thesis, in four links**, as the book's own branch on the author's earlier scenario analysis (arXiv:2607.07207) and graded [S]:
- agentic value migrates from the model to the harness and tools;
- a small model in a strong harness, iterating with review, substitutes for a frontier model run once;
- the market bifurcates into a mass tier and a luxury tier costing $18–38B a run by 2030;
- if the harness wins, the luxury tier becomes a niche that cannot finance the next run.

**Link one — model or harness — both sides are right, and the difference is decisive.**
- Among near-peer frontier models the harness dominates: one controlled factorial study finds harness variance 7.8× model variance, and on SWE-bench Verified the same model varies 15.6 points across scaffolds against a whole top-30 spread of 8.8.
- Across capability tiers the model dominates: 12–44-point model spreads against 3–8-point harness spreads on a public leaderboard.
- METR found that two leading proprietary harnesses did not significantly beat its plain scaffolds.
- The thesis needs cross-tier substitution; the harness-dominance evidence is almost all intra-tier.

**Link two — the "Claude Code + Qwen3.8-27B matches frontier one-shot" claim has no located source.**
- The only published pairing is the vendor's own single-attempt figure against the previous generation (61.7 vs 53.4).
- The independent decontaminated board has the predecessor model at 31.2% against 63.4–64.5%, at 5–35× lower cost per attempt — not two orders of magnitude.
- The test-time-scaling literature gives the sharper version the book adopts: **small-model iteration substitutes for the frontier on verifiable, short tasks and fails on unverifiable, long ones, so the premium tier does not vanish but retreats to the work a test suite cannot check.**

**Links three to five — bifurcation observed, saturation not.**
- Open weights took 56% of one gateway's August tokens on 14% of spend.
- The leading premium laboratory's run-rate rose roughly sevenfold in seven months, and hyperscaler capex was raised.
- Chapter 21's losses and the walk-back of compute commitments from ~$1.4T to $600B are printed alongside.
- Jev-style first tiers: the cascade literature supports inference savings of 45–98%, but no measured frontier-token reduction exists yet, and **no source anywhere links routing to lower training requirements — that half of the link is dropped.**

**On whether the Epoch training series is out of date.** The objection is correct as far as it goes: the series is fitted since 2020 on pre-training-dominated runs, with no agentic-era measurement. But RL compute scaled ~10× in four months, so the agentic era added an expensive stage rather than removing one. The best technical support for saturation is Toby Ord's finding that RL scales so poorly its gains mostly move cost from training to inference — the thesis's mechanism, arrived at from the technical side.

**The pacing calls, and the readings of them.**

What happened, in order:
- A July staff letter asked for international tools to "pace the frontier of automated AI development."
- On 18 August OpenAI paused its own RL training for two weeks. It cited two triggers: a Hugging Face breach, which Hugging Face confirms was agentic and which OpenAI's own report attributes to its research model; and a self-assessed "Critical" cyber threshold.
- On 12 September Anthropic's chief executive published an essay stating that "pacing does not mean halting model training." It proposed evaluators, democratic-country coordination under an antitrust waiver, and outreach to authoritarian governments.
- The essay was endorsed separately by OpenAI, xAI and Google DeepMind, and rejected by Meta, NVIDIA, the US President and China's Foreign Ministry.

Three readings are presented, each with what supports it and what cuts against it:
- **Face value** — 2023 continuity and a confirmed incident; against: no unilateral slowdown in the essay, silence on open weights, self-attributed triggers, a $45B compute deal two weeks earlier.
- **Regulatory moat** — the dominant critique, from the White House AI adviser and the FTC Chair; against: 2023 proposals predate the lead, external evaluators, signatories from outside the arrangement.
- **Return-on-investment retreat** — the book's own construction, since no named commentator was located advancing it in full; for: the trade chapter's losses and commitment walk-backs, and its compatibility with the moat reading; against: it requires the stated capability claim to be insincere, and premium revenue was still rising.

**The book does not adjudicate motive.** It states that the effect on training spend depends on *what is enacted*, not why it was proposed, and names the observable that separates the readings: capex cut under safety language, versus pacing that binds on release while the buildout continues.

**Consequence:** if saturation comes, by market or by agreement, it is the most favourable outcome in the book for the strategy of Part I. Four falsifiers are entered in the register.

### Related changes

- **Chapter 18 (trust):** the Hugging Face breach passage now records OpenAI's own attribution of the breach to its research model, graded as the company's attribution, with the open/closed security implication stated in both directions.
- **Chapter 11 (harness):** reconciled with the new evidence. The "one controlled study" and "no independent benchmark" statements are now scoped to *cost*; independent *score*-variance studies are acknowledged and cross-referenced.
- **Chapter 21 (trade):** hyperscaler capex figures updated for the Q2 raises (combined ~$720–745B).
- **Chapter 29 (summary):** now carries the saturation argument in one paragraph.

### Audit

An independent adversarial pass produced 22 findings, all applied. The most important was that **the first draft of the pacing subsection was tilted in the companies' favour**: counter-evidence was printed only against the ROI reading, the revenue growth was misstated as "tripling", the trade chapter's losses were omitted, and a third-party-confirmed breach was overstated as a third-party-confirmed attribution. The subsection was rewritten so that each reading carries its own evidence for and against. Other fixes:
- an unsourced claim about an unnamed laboratory, removed;
- an ungraded inference about a state's motive, removed;
- an over-strong continuity claim, corrected to "one rate limit, one conditional self-pause";
- a truncated quotation, restored;
- a missing fourth register row, added.

---

## v0.25 — 21 September 2026

**Full edition 415 pages, five parts, 29 chapters · Condensed edition 59 pages · 818 bibliography entries (30 new)**

The largest release since the five-part restructure. Four bodies of new material, of which the first changes an argument rather than adding to one.

### The cost collapse is a serving phenomenon (Chapter 10, new §10.7)

The book has argued P3 throughout on the strength of falling prices. This section establishes that **the falling prices are entirely on the serving side, and that the training curve runs the other way** — which is the most consequential single correction in this edition.

**The measurements.** MIT FutureTech prices *inference* at fixed benchmark performance and finds the cost–performance frontier falling **5–10× per year**, of which ~3× survives adjustment for hardware. Epoch AI's series — the only independent one tracking *training* — reports frontier training cost **rising about 3.5× per year since 2020**, a doubling time near seven months. DeepSeek's own V4.1-Flash report does not address pre-training cost at all: 45T tokens with no comparison to predecessors, every efficiency claim aimed at prefill, storage and decode.

**The one training claim in the window, read precisely.** Alibaba's **Qwen3.8-Flash-Next** (26 Aug; 125B total / **6B active**, plus 51B N-gram parameters designed to sit in *system* rather than accelerator memory — the memory arbitrage of Chapter 12 appearing inside a model architecture; hybrid Gated DeltaNet and sparse attention; 512 experts, 11 active; licence **`qwen-community-1.0`, not Apache**, a widely repeated error from confusion with Qwen3.8-27B) claims training at **~1/9** the cost of a comparable predecessor. Graded [P], unreplicated, and — decisively — **a claim about reaching a given capability for fewer GPU-hours, not about the frontier becoming cheaper to push outward**. The same rhetorical move was made a generation earlier for Qwen3-Next in September 2025.

**And the quantization tier is not what it is read as.** PrismML's **Ternary Bonsai 2 27B** (17 Sep, Apache, 1.76 bits/weight, 54GB → 5.9GB, ~2M downloads in a month) makes **no training claim and structurally cannot** — it is a *post-training* quantization **of Qwen3.8-27B**. An independent hands-on test found the 98.2% quality claim failing in practice, with complete failure on multilingual translation and a regression from Bonsai v1. The interesting fact is the base model: a venture-backed American startup compressed an open Chinese model ninefold and shipped it permissively without training anything — **the commons compounding, on top of someone else's training bill**.

**What the asymmetry does.** Worse for the book in one respect: if the barrier to *being* a frontier laboratory rises 3.5×/year while the rent from operating one falls 5–10×, the commons has **fewer and richer suppliers** each year. That is the strongest available objection to P1's supply side, and sharper than any objection to P4. Better in another: the strategy of Part I never required cheap training — it required the serving rent destroyed while the state absorbs the training bill, which is exactly what four prior campaigns did with capital no private firm would commit. Entered as a falsifier: an independent measurement of frontier training cost *falling* in 2027 repairs P1's supply side; continued rise makes "who can still afford to train" the most important unanswered question in the book.

### The harness swarm, the mortality, and five days in September (Chapter 11, two new sections)

**Proliferation and death at comparable rates.** A curated index tracked 106+ harnesses by July 2026. Between January and July **six shut down** — and **Phind's shutdown statement named "commoditisation by foundation-model providers" as the cause of death**. A company that died of this book's mechanism and said so is better evidence than the proliferation is.

**The sponsorship table is Chapter 17's argument in miniature** and is near-unbroken: DeepSeek, Anomaly, Nous, Alibaba and Moonshot all give the harness away and earn on *inference*; Microsoft keeps a proprietary one and earns on *seats* at $99/user/month. The cleanest case is same-day: **DeepSeek released an MIT-licensed Claude Code competitor on 13 August, the same day it launched V4-Pro with peak/off-peak tiering raising its own inference prices by 50% to over 1,100%.** The harness was not a product; it was a price move on the layer below. **OpenClaw** — the largest, and the only one with *no* adjacent revenue layer, a 501(c)(3) with no paid tier — is also the only one whose growth stalled: star velocity **−93%** and release cadence **−88%**, both inflecting in June 2026. At 389k stars and ~3.2M monthly actives, "growth flattened sharply" is defensible and "faded" is not.

**Nobody can say which harness is better, and that is a finding.** The flagship leaderboards **deliberately hold the harness constant** so that models can be compared; the one purpose-built harness-comparison leaderboard publishes no finalised scores; every cross-harness figure located is vendor self-reported, and one widely circulated comparison could not be substantiated at its cited source.

**Five days: §11.6.** On 15 September TypeSafe AI shipped **Jev**, a closed "System One Model" returning calibrated probabilities over a caller-defined schema at $0.042/M input, architecture and parameter count withheld. **The first open replications appeared on 17 September — two days later.** By the 20th there were twelve to fifteen, MIT or Apache where licensed at all, and a head-to-head benchmark existed. That benchmark puts the proprietary model first **by seven tenths of a point**, leading by 4.5 on intelligence and **10.1 on calibration** and losing decisively on cost. The decomposition is the finding: **what was cloned in 48 hours was the interface and the logit-reading trick, not the training method**, which remains unreproduced, and most open projects explicitly disclaim calibration. Two cautions the book prints because the errors are circulating: **"OpenJev" names at least four unrelated projects** (one a Minecraft bot framework), and **Laya's headline win is not like-for-like** — its 0.766 is a checkpoint fine-tuned on the benchmark's own training split against a zero-shot competitor; its *zero-shot* score is **0.362 against a 0.318 random baseline**, and on 77 labels it scores 0.425 against Jev's 0.870. The general proposition, falsifiable within a year: **when a layer is commoditized, what survives is the part that was hardest to measure, not the part that was hardest to build.**

### The moratorium question, both sides at full strength (Chapter 14, new §14.7)

**Mostly a taxonomy problem.** Exactly **one** statewide moratorium is in force — New York's EO 62 of 14 July, reaching only *discretionary state* environmental permits above 50 MW and **not local permits at all**. Pennsylvania's order is a conditional regime; Loudoun County voted only to *draft* one; Texas froze an interconnection queue; and **twelve of fourteen state "moratoria" are unpassed bills**.

**The two headline numbers measure different objects**: $130bn of projects "blocked or delayed" (media scan, no megawatt figures, undisclosed funders) against **2.3 GW actually delayed** of ~20 GW inside restricted areas — three projects accounting for nearly all of it — versus 38 GW forecast for 2027 delivery, i.e. about **6% of one year's delivery**.

**Both cases argued at their strongest.** For restriction: PJM billed **$6.2bn** of capacity cost against facilities *forecast but not built*, while clearing below its own reliability requirement at the price cap; Texas's queue holds **474 GW against a ~90 GW peak**; opposition runs 61–71%, exceeds 50% in *every* party group, and the House passed a ratepayer bill **417–3**. Against: **76–126 GW of headroom** exists for loads accepting curtailment of 0.25–1% of annual energy — thirty-three to fifty-five times what moratoria delay, with no new generation; Virginia's own legislative auditor found data centres **currently pay full cost of service**; the best-identified causal study finds they **lowered** retail rates 3.5% (with its weak first stage and EPRI affiliation printed); and a decomposition **commissioned by a consumer advocate** attributed $8.7bn of PJM's $12.5bn spike to an accreditation rule change and two plant retirements rather than to load.

**Why the studies disagree** turns out to be partly a category error the book can resolve: they measure *capacity*, *wholesale* and *retail* prices respectively, and fixed-cost spreading and marginal dispatch are both real and act on different components of the same bill. What is genuinely unresolved is whether the $6.2bn attributed to unbuilt facilities ever meets real load.

**Capacity is not fleeing abroad**, and the book says so explicitly — no source establishes it; what moved is *within* the US, Northern Virginia down 29% while Atlanta became the most active market. And the federal government has **expressly declined to preempt** local siting, carving data centres out of its own AI-preemption order.

### What the Chinese siting advantage actually bought (Chapter 14, new §14.6.7)

This cuts against a passage already in the book, and is written that way. The velocity advantage is real — 39 completed ultra-high-voltage lines, straightforward western interconnection. **The price advantage does not exist**: in the *coastal* provinces where Chinese data centres actually operate, industrial rates sit **near or above Virginia's**. East Data West Computing delivered measured energy savings of **4–12%** with negligible emissions or renewables benefit, and 75% of digital-industry income remains in East China. Against a 60% utilization target, **Beijing's own estimate is 20–30%**, with **100+ state-backed projects cancelled in eighteen months**. State siting authority bought velocity *and* bought stranded assets, and the two are causally linked. The utilization gap is entered in the register as the quantity that would settle it.

### The stack above the commodity (Chapter 23, new §23.4)

The corollary a middle power has to act on. A national planning decomposition of projected 2030 scientific compute demand — on the order of half a million accelerators — splits it **14% LLM token generation, procurable from any cloud, and 86% simulation, non-LLM training, data processing and experiment integration**, which nobody is organized to sell. **The entire contest this book describes is a fight over a seventh of a national scientific programme's compute.**

The position therefore sits *above* the commoditizing layers, in four that resist: an integrated execution substrate carrying simulation, data, training, inference and agents together; science-domain models that are explicitly *not* LLMs, whose training data is instrument output that must be generated rather than scraped; a harness through which simulations, datasets and *laboratory instruments* become callable tools; and autonomous scientific workflows whose loop terminates in physical apparatus. This **inverts the usual sovereignty prescription** — building a national foundation model and national accelerators enters the two layers where two superpowers are spending most heavily to drive price to marginal cost and where the commons is already adequate. The economic claim is a rent claim: a programme running its own substrate does not pay the cloud's margin on the 86%, and that margin is the one the book finds intact and large.

**Declared:** the source is a briefing the author prepared for a programme he directs. It is named as self-authored in the section, added to the front-matter declaration of interest, graded [P/M], and the section states three things it does not claim — a measured causal return, that the 86/14 split generalizes, or that the commodity layer is safe to ignore.

### Corrections applied to premises that did not survive verification

- **"Qwen-NEXT"** → Qwen3.8-Flash-Next (26 Aug 2026). A separate "Qwen3-Next" exists from **September 2025**; the two are not merged. Flash-Next is **not Apache**.
- **"Bonsai 2 brings costs down for inference and also for training"** → it is a post-training quantization and **makes no training claim**; the training half is deleted rather than hedged.
- **"JEV"** → **Jev**, and it is not a generative model.
- **"OpenJEV"** → at least four unrelated projects; the book names authors.
- **Laya's headline** → corrected to the like-for-like comparison with the zero-shot number printed.
- **"OpenCode sprang up after OpenClaw"** → OpenCode launched **19 June 2025**, seven months before the OpenClaw name existed; it is excluded from the successor list and identified as predating the wave.
- **"Hermis"** → **Hermes Agent** (Nous Research, 25 Feb 2026), which ships a one-command migration path importing OpenClaw installations.
- **"OpenClaw has faded"** → split into the half that survives (growth) and the half that does not (usage).
- **"harnesses that are much better"** → not verifiable; the absence of any controlled harness-versus-harness benchmark is reported as a finding.

### Consistency and audit

An independent adversarial pass produced 21 findings, all applied. Among them: a DeepSeek harness/price-rise date that contradicted itself in four places (resolved to same-day, matching the verified primary); eight relative-date phrases left stale by the nine-day move of the currency date; a curtailment figure stated in percent-of-time when the source means percent-of-energy; "roughly seventy per cent" sitting next to components summing to 90.3% on a different denominator; "thirty to fifty times" for a ratio that is 33–55; a sponsorship claim that did not hold for the two proprietary rows of its own table; a table caption contradicted by its own row; the strongest independent qualification of Jev's accuracy present in the bibliography but cited nowhere; a duplicate bibliography key; and an authorship disclosure that the book's own convention required and had omitted.

### Build

Both editions three-pass clean: **zero undefined references, zero undefined citations, zero duplicate labels, zero float-overflow warnings**, worst overfull hbox 16.7pt (all pre-existing). The model-timeline table was converted to a `longtable` to accommodate three new rows. Full edition 415 pages, condensed 59, 818 bibliography entries with no duplicate keys and no cited-but-missing keys in either edition.

---

## v0.24 — 12 September 2026

**Full edition 394 pages, five parts, 29 chapters · Condensed edition 57 pages · 788 bibliography entries (10 new)**

A minor release with two jobs: absorb DeepSeek's V4.1-Flash, and finish counting the fourth precedent that v0.23 added. Both turned into corrections. The model release does not do what the coverage says it does, and the precedent sweep found eleven surviving "three" constructions including the Part I title itself.

### DeepSeek V4.1-Flash (Chapter 10, new §10.3.5)

The claim arrived as "DeepSeek 4.1 Flash — the low cost, benchmark scores and tokens/s are amazing, but there are reported shortcomings especially on visual tasks." Three parts of that did not survive the check.

**The name.** It is **DeepSeek-V4.1-Flash**, API string `deepseek-flash`, released **10 September 2026**: a 552B mixture-of-experts backbone activating **8B on prefill and 16B on decode**, a forty-layer causal encoder–decoder, one shared plus 384 routed experts with six live per token, 1M context, 45T pre-training tokens, MIT, weights shipped. The same announcement **retired** `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` and silently re-routed the legacy identifiers — an operational hazard in its own right, and the reason the next correction is easy to make.

**The price is shaped, not simply low.** Off-peak $0.003 cached input / $0.15 uncached input / $0.60 output per million tokens; peak double. On the combined million-in, million-out basis this book orders its price table by, that is **$0.75 off-peak and $1.50 at peak — *above* GLM-5.3-Flash's $0.65 and above the retired predecessor's $0.42**, and at peak above GPT-5.6 Luna's $1.40. What is exceptional is one line the combined column cannot show: **cached input at $0.003**, roughly a seventh of the cheapest competing cached rate and a thirtieth to a hundred-and-sixtieth of the mid- and top tiers. That is a targeted subsidy of exactly one workload shape — the long, repeatedly re-read context of an agent loop — not a general cut. The ledger's own method changes as a result: vendors now price workload *shapes* rather than tokens, and future editions carry cached and uncached input as separate columns.

**The ordering survives a basis this book did not choose.** Artificial Analysis blends cache-hit, uncached and output tokens 7:2:1 and prices V4.1-Flash at **$0.18 per million against GLM-5.3-Flash's $0.10** — a different basis from the combined million-in, million-out figure above, and the same result. The "not actually the cheapest" finding therefore does not rest on an arithmetic basis of the author's choosing.

**The index went the other way.** On Artificial Analysis **v4.3** the model scores **40** — *behind* GLM-5.3-Flash's 42 and level with Qwen3.8. The new price leader is not the strongest model in its own weight class. The "50" circulating for its predecessor belongs to an **earlier index version**, where the same checkpoint re-scores **35**; any narrative of a decline from 50 to 40 compares two instruments rather than observing a model. DeepSeek's own table shows why: Terminal-Bench **2.1 at 90.6**, a win over Claude Opus 5's 89.1 — but **30.0 on v3.0** against 43.3 and **31.2 on v4.0** against 51.8. It wins the superseded variant and loses the two current ones by thirteen and twenty-one points, and Terminal-Bench v4.0 is one of the ten components of the v4.3 index. Strong when bounded and single-shot, weak when long-horizon and agentic.

**The visual shortcomings belong to a different model.** V4.1-Flash is **natively multimodal** — a DeepSeek-ViT encoder with visual and text embeddings trained jointly from the start of pre-training — and **no independent third-party vision evaluation of it exists**: Artificial Analysis publishes no multimodal index and the public arena has not listed it. The concrete failures circulating in early coverage (an exponent absorbed into a multi-digit number, an Urdu passage dropped and a word hallucinated into an Indonesian handwriting sample, images tokenized at a fixed 384-token ceiling regardless of resolution) are tests of **DeepSeek-V4-Flash-Vision-Exp**, shipped 21 August and **retired on 10 September**, the same day the old identifier was pointed at the new model. The register entry for V4.1-Flash vision is therefore **"not measured," not "weak."** What *is* anomalous, and is recorded as a signal rather than a measurement: DeepSeek published vision numbers for the **base model only** and, uniquely among the sections of its suite, **with no competitor columns at all** — MMMU-Pro 56.5, CVBench 77.9, DocVQA 95.6, RefCOCO-avg 86.0, with **no MathVista, ChartQA, OCRBench or non-Pro MMMU** — and the instruct model's visual figures are **tool-assisted** (ZeroBench 49.0 *with Python*).

**Speed holds, with the spread printed.** 217 output tokens/s and 1.13s time-to-first-token on DeepSeek's own endpoint against GLM-5.3-Flash's 98 and 2.49s — genuine leadership in the bracket — but the same aggregator's provider page says 199 and OpenRouter measures 127 as best of eleven providers, so the book quotes a band of roughly 125–220 rather than a number. And no source establishes what silicon served the measured requests, so the throughput figure is connected to neither the Cambricon day-zero adaptation nor DeepSeek's reported Ascend order.

**The vendor's own caveats are the most useful in the file.** DeepSeek concedes that "CSA2 sparse-selection errors" and "approximate state reconstruction" can degrade output in extended-context sparse retrieval and at cache-resumption boundaries — a long-context fragility located precisely in the mechanism that produces the cheap KV cache, so the efficiency and the failure mode share a cause. And raising reasoning effort from 25 to 100 costs **~2.5× the output tokens**, which is the setting every headline benchmark uses.

**What it does to the argument, and what it does not.** It confirms the open-weight ratchet at a **fifth consecutive frontier-family release to ship weights** (Kimi K3, Qwen3.8-Max, GLM-5.3, GLM-5.3-Flash, and this), on the most permissive terms any frontier-scale Chinese model carries. It cuts *against* two of the book's readings, both conceded in the text: **local deployment got harder, not easier** — from a 280B predecessor to a 552B backbone plus ~196B of resident N-gram weights and a floor in the high hundreds of gigabytes at FP8, so the personal-and-SME-hardware argument that made GLM-5.3-Flash strategically interesting does not transfer; and it does **nothing for Proposition P2**, since the integration test is *training* on domestic silicon and the customer best placed to buy that capacity has reportedly ordered it for inference only. One line of the price surface moved. The frontier did not.

One methodological note recorded in both editions: the N-gram / conditional-memory construction behind the efficiency is **convergent industry practice** — Alibaba's Qwen3.8-Flash-Next and Google's Gemma line use comparable schemes — not a unilateral Chinese breakthrough. And the secondary account supplying the 763B total and the 567GB FP8 floor does not reconcile with itself (552 + 196 = 748), so the book takes the order of magnitude and not the figure, and says so.

### The fourth precedent, counted through (both editions)

v0.23 added the telecommunications campaign as a fourth Part I precedent but left the arithmetic of the earlier text alone. This release finishes it. **Part I is now "The Precedents: Four Wars Already Won."** Updated: the thesis chapter's opening section ("Four wars, one playbook") and its enumeration; the playbook chapter's "four surveys" and its table caption, which now states explicitly that the table covers the three commodity wars and that telecommunications is scored against the six steps in its own chapter rather than tabulated; "a playbook from four campaigns"; "won four technology wars" (three sites); "four precedent campaigns as its track record"; "four industrial precedents"; "a playbook argued from four victories" (both editions); Europe "having sat out the manufacturing of all four precedents"; the summary chapter's precedent sentence, which now names the switch alongside the cell, the pack and the car; and the front-matter definition of winning, which now includes the network case. The condensed edition's preface, thesis chapter, precedent chapter and summary carry the same corrections.

**One ordinal decision, stated because it is a judgment.** "Why AI is the fourth war" becomes **"Why AI is the next war,"** and the strategy chapters now describe the playbook run on "a fifth industry." The ordinal was only ever counting *commodity* campaigns; with a network precedent in Part I it either has to move or has to keep being maintained, and the version that cannot drift is the one without a number in it.

**Added to the claim register:** three telecommunications rows (Huawei's flat 31% share across the sanctions period, the CDB facility and the state-support reconstruction, and the finding that the bans bit only where security agencies held a veto) — a fourth precedent with no register entry was a structural gap.

### Other consistency fixes

- §10.5 retitled **"Five frontiers, three scoreboards"**: the section opened by describing five frontiers under a heading that said three.
- The model-timeline table's caption ran to "August 2026" over a table that now ends in September, and said "Chinese" over a table containing Meta's Muse Glimmer; both fixed.
- Two relative-date phrases ("in the last week before this edition's currency date," "in the week before") were stale by more than a fortnight after the currency date moved to 12 September; both now state the real interval.
- The trust chapter's "on the currency date itself" for the 9 September NSA/FBI/CISA advisory is now "three days before the currency date."
- The theory chapter's "Part I shows this sequence completing three times" is now scoped to three of Part I's four campaigns, since the below-cost mechanism is commodity-specific.
- The bulletin appendix's closing "Strengthened: three things" is now four, accounting for its own newest section.

### Build

Both editions rebuilt three-pass: **zero undefined references, zero undefined citations, zero duplicate labels, no float-overflow warnings**, worst overfull hbox 16.7pt (pre-existing). Full edition 394 pages, condensed 57 pages, 788 bibliography entries with no duplicate keys and no cited-but-missing keys in either edition.

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
