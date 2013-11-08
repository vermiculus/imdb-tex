IDS=tt0134273 tt0050083 tt0057181
TEMPLATE=imdb-template.tex


grab:
	./imdb.py $(TEMPLATE) $(IDS)

tex:
	pdflatex $(TEMPLATE)
        pdflatex $(TEMPLATE)

all: grab tex
