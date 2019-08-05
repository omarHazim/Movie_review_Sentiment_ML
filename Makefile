.PHONY : all clean 

IRIS_URL  = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/irise.data"


all : data/raw/iris.csv

clean:
	rm -f data/raw/*.csv

data/raw/iris.csv:
	python data/raw/download.py $(IRIS_URL) $@


