#!/bin/sh

rm -fr Puzzles/
mkdir Puzzles/

for TEMPLATE in 1 1 2 3 4 5  ; do
	for iteration in 1 2 3 ; do
		cp Prosperity-7-Template-${TEMPLATE}.xml in.xml
# Because of a bug in my Java hack, we have to interact with a dialog
# to make a valid out.xml :(
		touch out.xml
		Java -jar SudokuGenerate.jar
		mv out.xml Puzzles/$( cat out.xml | \
			cut -f8 -d\" | tr -d ' ' | \
			tr -d '\r' | tr -d '\n')-$( date +%s ).xml
		sleep 1
	done
done
