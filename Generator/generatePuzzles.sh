#!/bin/sh

rm -fr Puzzles/
mkdir Puzzles/

for iteration in $( awk 'BEGIN{for(a=1;a<=2;a++){print a}}' ) ; do
	for TEMPLATE in 1 1 2 3 4 5  ; do
		cp Prosperity-7-template-${TEMPLATE}.xml in.xml
		rm -f 1.xml 2.xml 3.xml 4.xml 5.xml 6.xml 7.xml 8.xml \
			9.xml 10.xml 11.xml 12.xml 13.xml 14.xml \
			15.xml 16.xml 17.xml 
		java -jar SudokuGenerate.jar > /dev/null 2>&1
		for num in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 ; do
			mv ${num}.xml Puzzles/$( cat ${num}.xml | \
				cut -f8 -d\" | tr -d ' ' | \
				tr -d '\r' | \
				tr -d '\n')-$( date +%s \
				)-${TEMPLATE}-${iteration}-${num}.xml
		done
		echo $TEMPLATE $iteration
	done
done

