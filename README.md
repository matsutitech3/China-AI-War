# How China Will Win the AI War

### The Convergence Strategy: A Structural Path to AI Dominance

**Satoshi Matsuoka** — Director, RIKEN Center for Computational Science (R-CCS); Professor, Institute of Science Tokyo

**Current edition: v0.16.1 — 15 August 2026** · [Download the PDF](How-China-Will-Win-the-AI-War-v0.16.1.pdf) · 249 pages

---

## About

This is a **living book**. It argues that China's position in artificial intelligence should be read not as a race between models but as the fourth run of an industrial playbook that has already won three technology wars — solar photovoltaics, lithium-ion batteries, and electric vehicles — in each of which the West began holding the science, the patents, the firms, and the markets.

"Winning" here does not mean producing the single best frontier model in any given quarter. It means what winning meant in those three industries: capturing the overwhelming majority of global production, setting the cost curve, controlling the supply chain, defining the de facto standards, and reducing erstwhile leaders to protected niches sustained by tariffs and subsidies.

The book is deliberately falsifiable. Four load-bearing propositions are stated separately, coupled, and given their own falsification conditions. Every headline claim carries an evidence grade. A machine-readable claim register and a quarterly falsification dashboard are printed as appendices, and the fastest route to the argument's weakest link is to read the graded ledger first.

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

## Data

[`funnel-model.csv`](funnel-model.csv) contains the pessimistic/central/optimistic parameter triples for the AI-for-Science value-conversion funnel, by task class. The book's headline figures — a task-weighted central estimate near 11%, a 10th–90th percentile range of roughly 8–18% — are reproducible from this file. Recompute or re-weight it and the model's conclusions move with you; that is the point of publishing it.

## Building from source

The manuscript builds with a standard TeX Live installation and `pdflatex` (no `bibtex` — the bibliography is a manual `thebibliography` environment):

```bash
make            # three passes, resolves all cross-references
make clean      # remove build artifacts
```

Or directly:

```bash
pdflatex main.tex && pdflatex main.tex && pdflatex main.tex
```

Every push to `main` rebuilds the PDF via GitHub Actions, so the committed source and the published PDF never drift apart.

## Citing

```bibtex
@book{matsuoka2026china,
  author    = {Matsuoka, Satoshi},
  title     = {How China Will Win the AI War: The Convergence Strategy---A Structural Path to AI Dominance},
  year      = {2026},
  note      = {Living book, v0.16.1, 15 August 2026},
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
