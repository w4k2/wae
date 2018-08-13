all: experiments collect analyze

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

clean:
	rm results/*
	rm figures/*
