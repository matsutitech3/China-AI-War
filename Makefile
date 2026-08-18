LATEX   := pdflatex
FLAGS   := -interaction=nonstopmode -halt-on-error
MAIN    := main
VERSION := v0.20.1
OUT     := How-China-Will-Win-the-AI-War-$(VERSION).pdf
COND    := How-China-Will-Win-the-AI-War-Condensed-$(VERSION).pdf

SRC  := $(MAIN).tex $(wildcard chapters/*.tex) $(wildcard figs/*.tex)
CSRC := condensed/$(MAIN).tex $(wildcard condensed/chapters/*.tex) $(wildcard condensed/figs/*.tex)

.PHONY: all full condensed clean distclean check check-condensed

all: full condensed

# --- Full edition -----------------------------------------------------------
full: $(OUT)

$(OUT): $(MAIN).pdf
	cp $(MAIN).pdf $(OUT)

$(MAIN).pdf: $(SRC)
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex
	$(LATEX) $(FLAGS) $(MAIN).tex

# --- Condensed edition (same version stamp; built from condensed/) ----------
condensed: $(COND)

$(COND): condensed/$(MAIN).pdf
	cp condensed/$(MAIN).pdf $(COND)

condensed/$(MAIN).pdf: $(CSRC)
	cd condensed && $(LATEX) $(FLAGS) $(MAIN).tex
	cd condensed && $(LATEX) $(FLAGS) $(MAIN).tex
	cd condensed && $(LATEX) $(FLAGS) $(MAIN).tex

# Fail loudly on unresolved cross-references or citations.
check: $(MAIN).pdf
	@! grep -q "Reference.*undefined" $(MAIN).log || { echo "UNDEFINED REFERENCES"; exit 1; }
	@! grep -q "Citation.*undefined" $(MAIN).log || { echo "UNDEFINED CITATIONS"; exit 1; }
	@! grep -q "multiply defined" $(MAIN).log || { echo "MULTIPLY DEFINED LABELS"; exit 1; }
	@echo "OK: no undefined references, citations, or duplicate labels."

check-condensed: condensed/$(MAIN).pdf
	@! grep -q "Reference.*undefined" condensed/$(MAIN).log || { echo "UNDEFINED REFERENCES (condensed)"; exit 1; }
	@! grep -q "multiply defined" condensed/$(MAIN).log || { echo "MULTIPLY DEFINED LABELS (condensed)"; exit 1; }
	@echo "OK: condensed edition has no undefined references or duplicate labels."

clean:
	rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc $(MAIN).lof $(MAIN).lot
	rm -f condensed/$(MAIN).aux condensed/$(MAIN).log condensed/$(MAIN).out condensed/$(MAIN).toc condensed/$(MAIN).lof condensed/$(MAIN).lot

distclean: clean
	rm -f $(MAIN).pdf $(OUT) condensed/$(MAIN).pdf $(COND)
