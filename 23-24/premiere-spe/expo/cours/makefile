prefixe=$(shell basename $(PWD))
suffixe=$(shell basename $(shell dirname $(PWD)))
title=$(prefixe)-$(suffixe)
pdf: $(title).tex
	latexmk --pdf $(title).tex
	evince $(title).pdf &
