LATEX   := pdflatex
FLAGS   := -interaction=nonstopmode -halt-on-error
MAIN    := main
VERSION := v0.15
OUT     := How-China-Will-Win-the-AI-War-$(VERSION).pdf

SRC := $(MAIN).tex $(wildcard chapters/*.tex) $(wildcard figs/*.tex)

.PHONY: all clean distclean check

all: $(OUT)

$(OUT): $(MAIN).pdf
	cp $(MAIN).pdf $(OUT)

$(MAIN).pdf: $(SRC)
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex

# Fail loudly on unresolved cross-references or citations.
check: $(MAIN).pdf
	@! grep -q "Reference.*undefined" $(MAIN).log || { echo "UNDEFINED REFERENCES"; exit 1; }
	@! grep -q "Citation.*undefined" $(MAIN).log || { echo "UNDEFINED CITATIONS"; exit 1; }
	@! grep -q "multiply defined" $(MAIN).log || { echo "MULTIPLY DEFINED LABELS"; exit 1; }
	@echo "OK: no undefined references, citations, or duplicate labels."

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot

distclean: clean
	rm -f $(MAIN).pdf $(OUT)
