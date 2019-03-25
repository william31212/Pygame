#!/bin/bash

echo Profiling...
python3 -m cProfile -o $1.pstats $1.py
echo Gen report png...
python3 -m gprof2dot -f pstats $1.pstats | dot -T png -o $1.png

echo Delete the data
rm -f ./$1.pstats

if [ "`uname`" == "Darwin" ]; then
	open ./$1.png
else
	start ./$1.png
fi