IDS=tt0 tt1 tt2 tt3 tt4 tt5 tt6 tt7 tt8 tt9 tt10 tt11 tt12 tt13 tt14 tt15 tt16 tt17 tt18 tt19 tt20 tt21 tt22 tt23 tt24 tt25 tt26 tt27 tt28 tt29 tt30 tt31 tt32 tt33 tt34 tt35 tt36 tt37 tt38 tt39 tt40 tt41 tt42 tt43 tt44 tt45 tt46 tt47 tt48 tt49 tt50 tt51 tt52 tt53 tt54 tt55 tt56 tt57 tt58 tt59 tt60 tt61 tt62 tt63 tt64 tt65 tt66 tt67 tt68 tt69 tt70 tt71 tt72 tt73 tt74 tt75 tt76 tt77 tt78 tt79 tt80 tt81 tt82 tt83 tt84 tt85 tt86 tt87 tt88 tt89 tt90 tt91 tt92 tt93 tt94 tt95 tt96 tt97 tt98 tt99
DEMOIDS=tt0134273 tt0050083 tt0057181
TEMPLATE=imdb-template.tex

install:
	chmod +x imdb.py

demo:
	./imdb.py $(TEMPLATE) $(DEMOIDS)

grab:
	./imdb.py $(TEMPLATE) $(DEMOIDS) $(IDS)

tex:
	pdflatex $(TEMPLATE)
	pdflatex $(TEMPLATE)

all: grab tex
