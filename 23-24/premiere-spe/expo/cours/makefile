prefixe=$(shell basename $(PWD))
suffixe=$(shell basename $(shell dirname $(PWD)))
title=$(prefixe)-$(suffixe)
pdf: $(title).tex
	cp $(title).tex $(title)-dys.tex
	latexmk -c --pdf $(title)-dys.tex
	sed '10,13d' $(title).tex > $(title)-all.tex
	mv $(title)-all.tex $(title).tex
	latexmk --pdf $(title).tex 
	mv $(title)-dys.tex $(title).tex
	evince $(title).pdf &
