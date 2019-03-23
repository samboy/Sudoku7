#!/bin/sh

rm -fr Puzzles/
mkdir Puzzles/

for TEMPLATE in 1 1 2 3 4 5  ; do
	for iteration in 1 2 3 ; do
		cp Prosperity-7-Template-${TEMPLATE}.xml in.xml
		rm -f out.xml
		Java -jar SudokuGenerate.jar > /dev/null 2>&1
		mv out.xml Puzzles/$( cat out.xml | \
			cut -f8 -d\" | tr -d ' ' | \
			tr -d '\r' | tr -d '\n')-$( date +%s ).xml
		sleep 1
	done
done
