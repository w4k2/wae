all: nods experiments collect analyze

nods:
	rm streams/.DS_Store

experiments:
	python -W ignore experiment_1.py

collect:
	python -W ignore collect.py

analyze:
	python analyze.py


get_data:
	wget https://github.com/w4k2/benchmark_streams/releases/download/0.1/bare_streams.zip
	unzip bare_streams.zip -d streams
	rm bare_streams.zip

moa:
	java -cp moa/moa.jar -javaagent:moa/sizeofag-1.0.0.jar moa.gui.GUI

clean:
	rm results/*
	rm figures/*

.PHONY: moa
