# How China Will Win the AI War

### The Convergence Strategy: A Structural Path to AI Dominance

**Satoshi Matsuoka** — Director, RIKEN Center for Computational Science (R-CCS); Professor, Institute of Science Tokyo

**Current edition: v0.20 — 18 August 2026** · [Full edition (PDF)](How-China-Will-Win-the-AI-War-v0.20.pdf) · 290 pages · [Condensed edition (PDF)](How-China-Will-Win-the-AI-War-Condensed-v0.20.pdf) · 48 pages

---

## About

This is a **living book**. It argues that China's position in artificial intelligence should be read not as a race between models but as the fourth run of an industrial playbook that has already won three technology wars — solar photovoltaics, lithium-ion batteries, and electric vehicles — in each of which the West began holding the science, the patents, the firms, and the markets.

"Winning" here does not mean producing the single best frontier model in any given quarter. It means what winning meant in those three industries: capturing the overwhelming majority of global production, setting the cost curve, controlling the supply chain, defining the de facto standards, and reducing erstwhile leaders to protected niches sustained by tariffs and subsidies.

The book is deliberately falsifiable. Four load-bearing propositions are stated separately, coupled, and given their own falsification conditions. Every headline claim carries an evidence grade. A machine-readable claim register and a quarterly falsification dashboard are printed as appendices, and the fastest route to the argument's weakest link is to read the graded ledger first.

## Two editions

The **full edition** is the authoritative record: every claim cited to its source, graded, and carried in the evidence ledger, claim register, and quarterly dashboard.

The **condensed edition** (`condensed/`, under fifty pages) is for readers who want the shape of the argument rather than the layers: what is being claimed, why, what would prove it wrong, and what it means for a government, laboratory, or company that is neither in Washington nor in Beijing. Part I's precedent campaigns are summarized in a single chapter; the weight is shifted toward the overall strategy and its international consequences. Nothing in it is new — every number, grade, and forecast is drawn from the full edition of the same version and date, and pointers into the full edition are marked *[full edition, Ch. n]* throughout.

## Structure

**Part I — The Precedents.** How the solar, battery, and EV wars were actually fought and won, the playbook abstracted from them, and — in a chapter of equal weight — the campaigns where the same playbook has *not* worked: commercial aircraft, lithography, machine tools, operating systems, biotechnology.

**Part II — The Elements of AI.** The model, the compute, the semiconductor, the watt, the data, and embodied AI, each analysed separately before being recombined.

**Part III — The Consequences.** Trust and agentic security, governance, the financial exposure of the incumbents, national strategies, how much compute a nation's science actually needs, and the international institution the analysis keeps arriving at.

## Reading apparatus

| Device | What it does |
|---|---|
| Evidence grades `[V] [P] [A] [M] [R] [S]` | Verified, primary, analyst, author-modeled, roadmap, scenario |
| Propositions P1–P4 | The four load-bearing claims, falsified separately |
| Claim register CR-01–CR-12 | Machine-readable, with a next verification event per claim |
| Currency date | Every fact in the stable chapters is current as of the edition date on the title page — the cutoff *is* the edition date, so it cannot contradict the book |
| Notation glossary | Front matter; a strict suffix discipline means no bare single letter carries two meanings |
| Technical dossiers | Appendix A (the LPDDR6X socket) and Appendix B (High Bandwidth Flash: lineage, announcement record, the OCP specification and its omissions, power, endurance, cost structure, the debate, the literature) — every load-bearing hardware assumption in Chapter 10 checked against the primary record |

## Data

[`models/appliance-vs-rubin.py`](models/appliance-vs-rubin.py) is the cost model behind §10.9's head-to-head of a capacity-first local appliance (2 TB HBF + 256 GB LPDDR6X) against a Vera Rubin NVL72 rack and the August 2026 API price list, on Kimi K3. Every BOM component is anchored to a finished, shipping, pre-surge system (ASUS Ascent GX10, Framework Desktop, pre-surge 1 TB NVMe retail) rather than to a bare-component guess, and both sides are fully loaded: the rack carries its building ($/W from the author's datacentre-construction survey, cross-checked against Epoch AI, JLL and CBRE wholesale rents), facility operations, and an 8% cost of capital, with a utilization sensitivity; the appliance carries a closet UPS, a small-room PUE and the same cost of capital. Every number in the table derives from stated inputs; change an input and re-run.

[`funnel-model.csv`](funnel-model.csv) contains the pessimistic/central/optimistic parameter triples for the AI-for-Science value-conversion funnel, by task class. The book's headline figures — a task-weighted central estimate near 11%, a 10th–90th percentile range of roughly 8–18% — are reproducible from this file. Recompute or re-weight it and the model's conclusions move with you; that is the point of publishing it.

## Building from source

The manuscript builds with a standard TeX Live installation and `pdflatex` (no `bibtex` — the bibliography is a manual `thebibliography` environment):

```bash
make            # both editions, three passes each
make full       # full edition only  -> How-China-Will-Win-the-AI-War-<version>.pdf
make condensed  # condensed edition  -> How-China-Will-Win-the-AI-War-Condensed-<version>.pdf
make check check-condensed   # fail on unresolved references
make clean      # remove build artifacts
```

Or directly:

```bash
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex          # full edition
cd condensed && pdflatex main.tex && pdflatex main.tex && pdflatex main.tex   # condensed edition
```

Every push to `main` rebuilds both PDFs via GitHub Actions, so the committed source and the published PDF never drift apart.

## Citing

```bibtex
@book{matsuoka2026china,
  author    = {Matsuoka, Satoshi},
  title     = {How China Will Win the AI War: The Convergence Strategy---A Structural Path to AI Dominance},
  year      = {2026},
  note      = {Living book, v0.20, 18 August 2026},
  url       = {https://github.com/matsutitech3/China-AI-War}
}
```

See [`CITATION.cff`](CITATION.cff) for the machine-readable form.

## Corrections

Corrections are welcome and will be credited. The quickest way to change this book's conclusions is to falsify an entry in the evidence ledger — open an issue naming the claim ID and the contrary evidence. Disagreement about interpretation is welcome too, but a dated primary source moves the argument faster than an argument does.

## Licence

The manuscript is released under [Creative Commons Attribution 4.0 International](LICENSE) (CC BY 4.0). You may share and adapt it for any purpose, including commercially, provided you give appropriate credit and indicate whether changes were made.

## Declaration of interest

The author directs a national supercomputing centre with longstanding working relationships across the Western AI and HPC industry, and is a participant in several of the Western programs the book discusses. Those interests are stated in full in the preface, where the argument is also made that they cut *against* this book's conclusion rather than for it.
