#!/usr/bin/env python

# Technical debt: The interface for adding a custom font doesn't actually
# work the way Weasyprint's documentation says it is supposed to work.
# I may just have to make Caulixtle008 a system font, and do things the
# way we did with older versions of WeasyPrint (yes, I have had to tell
# DevOps in a previous job "When you make a server which runs this program, 
# you must install this font following these steps, otherwise Weasyprint 
# will not correctly render")

# This uses the version of Python included with CentOS 7 (Python2)

import sys, re
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

try:
	outputFile = sys.argv[1]
except:
	print "Usage: genPdf.py {PDF output file} {XML file1} {XML file2} ..."
	sys,exit(1)

# This does not actually work...
font_config = FontConfiguration()

# The HTML used to make puzzles

puzzleTemplate = """
<table>
<tr>
<td class=a>Q11</td>
<td class=b>Q12</td>
<td class=b>Q13</td>
<td class=a>Q14</td>
<td class=a>Q15</td>
<td class=b>Q16</td>
<td class=c>Q17</td>
<tr>
<td class=d>Q21</td>
<td class=e>Q22</td>
<td class=e>Q23</td>
<td class=d>Q24</td>
<td class=a>Q25</td>
<td class=d>Q26</td>
<td class=f>Q27</td>
<tr>
<td class=d>Q31</td>
<td class=a>Q32</td>
<td class=b>Q33</td>
<td class=i>Q34</td>
<td class=d>Q35</td>
<td class=d>Q36</td>
<td class=f>Q37</td>
<tr>
<td class=a>Q41</td>
<td class=i>Q42</td>
<td class=a>Q43</td>
<td class=b>Q44</td>
<td class=i>Q45</td>
<td class=a>Q46</td>
<td class=g>Q47</td>
<tr>
<td class=a>Q51</td>
<td class=b>Q52</td>
<td class=d>Q53</td>
<td class=a>Q54</td>
<td class=b>Q55</td>
<td class=i>Q56</td>
<td class=h>Q57</td>
<tr>
<td class=d>Q61</td>
<td class=e>Q62</td>
<td class=d>Q63</td>
<td class=d>Q64</td>
<td class=a>Q65</td>
<td class=b>Q66</td>
<td class=j>Q67</td>
<tr>
<td class=la>Q71</td>
<td class=lb>Q72</td>
<td class=lc>Q73</td>
<td class=la>Q74</td>
<td class=la>Q75</td>
<td class=lb>Q76</td>
<td class=ld>Q77</td>
<tr>
</table>
"""

# The CSS for puzzles
puzzleCSS = """@font-face {
    font-family: 'Caulixtla';
    src: url('Caulixtla008.woff')
         format('woff');
}
body { font-family: Caulixtla; }
.p7p {
	font-family: Caulixtla;
        font-size: x-large;
        margin: 0;
        padding: 0;
        border-collapse: collapse;
}
.p7p table {
	font-family: Caulixtla;
        font-size: x-large;
        margin: 0;
        padding: 0;
        border-collapse: collapse;
}
.p7p td {
	padding: 1em;
}
.p7p td table td {
        width: 1em;
        height: 1em;
        padding: .1em;
        border-collapse: collapse;
        text-align: center;
}
.a {
        border-left: 3px solid black;
        border-top: 3px solid black;
}
.b      {
        border-left: 1px solid black;
        border-top: 3px solid black;
}
.c      {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
}
.d {
        border-left: 3px solid black;
        border-top: 1px solid black;
}
.e      {
        border-left: 1px solid black;
        border-top: 1px solid black;
}
.f      {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
}
.g      {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
}
.h      {
        border-left: 3px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
}
.i      {
        background-position: left top;
        background-repeat: no-repeat;
        border-left: 1px solid black;
        border-top: 1px solid black;
}
.j      {
        background-position: left top;
        background-repeat: no-repeat;
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
}
.la     {
        border-left: 3px solid black;
        border-top: 1px solid black;
        border-bottom: 3px solid black;
}
.lb     {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-bottom: 3px solid black;
}
.lc     {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-bottom: 3px solid black;
}
.ld     {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
}
"""

# Here, 0 means "blank space"
if len(sys.argv) <= 2:
	puzzleQuestion = [[6,0,4,0,2,0,3,0,5,0,0,0,1,0,1,0,0,2,0,0,4,0,0,7,0,
		6,0,0,4,0,0,5,0,0,2,0,1,0,0,0,6,0,3,0,5,0,1,0,7]]
else:
	puzzleQuestion = []
	for index in range(2,len(sys.argv)):
		f = open(sys.argv[index])
		i = f.read()
		q = re.split('\n+',i)
		q = q[1]
		q = re.sub('.*question difficult[^>]*>','',q)
		q = re.sub('</question.*','',q)
		z = re.split(' ',q)
		puzzleQuestion.append(z)

allHTML = "<div class=p7p><table><tr><td>"
for puzzle in range(len(puzzleQuestion)):
	index = 0
	puzzleHTML = puzzleTemplate
	for column in range(1,8):
		for row in range(1,8):
			replace = "Q" + str(column) + str(row)	
			thisNumber = puzzleQuestion[puzzle][index]
			if int(thisNumber) == 0:
				thisNumber = "&nbsp;"
			puzzleHTML = re.sub(replace,str(thisNumber),puzzleHTML)
			index += 1
	allHTML += puzzleHTML	
	if (puzzle % 2) == 0:
		allHTML += "</td><td>"
	else:
		allHTML += "</td></tr><tr><td>"

allHTML += "</td></tr></table></div>"

html = HTML(string=allHTML)
css = CSS(string=puzzleCSS, font_config = font_config)
html.write_pdf(outputFile, stylesheets=[css], font_config=font_config)

print outputFile + " written"
