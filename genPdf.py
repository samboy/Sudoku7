#!/usr/bin/env python

# This uses the version of Python included with CentOS 7 (Python2)
# The code also works with Python3

# While the puzzles look perfectly fine using the Weasyprint
# default font, one can optionally install the Caulixtla008.woff
# font.  See this page for notes:
# https://weasyprint.readthedocs.io/en/latest/features.html#fonts
# Example #1 (Windows + Cygwin, should work elsewhere) (remove hashes):

# mkdir ~/.fonts
# cp Caulixtla008.woff ~/.fonts

# Example #2 (CentOS 7 system-level install) (remove hashes):

# mkdir /usr/share/fonts/Caulixtla008
# cp Caulixtla008.woff /usr/share/fonts/Caulixtla008/
# fc-cache

import sys, re
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

try:
        outputFile = sys.argv[1]
except:
        print("Usage: genPdf.py {PDF output file} {XML file1} {XML file2} ...")
        sys,exit(1)

dupCheckOnly = False
dupsFound = False
if outputFile == "dupcheck":
    dupCheckOnly = True
if outputFile == "dup":
    dupCheckOnly = True

if (not dupCheckOnly) and (not re.search('\.[pP][dD][fF]$',outputFile)):
        print("Output file must be a .pdf file, e.g. genPdf.py foo.pdf")
        sys.exit(1)

title = outputFile
title = re.sub('.[pP][dD][fF]$','',title)

# This does not actually work...
font_config = FontConfiguration()

# Helper function: Given a string of numbers between 1 and 9, normalize
# the numbers so that 1 is the first unique number, 2 is the second unique
# number, and so on
def normString(i):
        map = {}
        max = 1
        out = ""
        for c in i:
                if not c in map.keys():
                        map[c] = str(max)
                        max += 1
                        if max >= 10:
                                print("Warning: normString too many numbers")
                                max = 0
                out += map[c]
        return out

# The HTML used to make puzzles

puzzleTemplate = """
<table>
<tr>
<td class=K11>Q11</td>
<td class=K12>Q12</td>
<td class=K13>Q13</td>
<td class=K14>Q14</td>
<td class=K15>Q15</td>
<td class=K16>Q16</td>
<td class=K17>Q17</td>
<tr>
<td class=K21>Q21</td>
<td class=K22>Q22</td>
<td class=K23>Q23</td>
<td class=K24>Q24</td>
<td class=K25>Q25</td>
<td class=K26>Q26</td>
<td class=K27>Q27</td>
<tr>
<td class=K31>Q31</td>
<td class=K32>Q32</td>
<td class=K33>Q33</td>
<td class=K34>Q34</td>
<td class=K35>Q35</td>
<td class=K36>Q36</td>
<td class=K37>Q37</td>
<tr>
<td class=K41>Q41</td>
<td class=K42>Q42</td>
<td class=K43>Q43</td>
<td class=K44>Q44</td>
<td class=K45>Q45</td>
<td class=K46>Q46</td>
<td class=K47>Q47</td>
<tr>
<td class=K51>Q51</td>
<td class=K52>Q52</td>
<td class=K53>Q53</td>
<td class=K54>Q54</td>
<td class=K55>Q55</td>
<td class=K56>Q56</td>
<td class=K57>Q57</td>
<tr>
<td class=K61>Q61</td>
<td class=K62>Q62</td>
<td class=K63>Q63</td>
<td class=K64>Q64</td>
<td class=K65>Q65</td>
<td class=K66>Q66</td>
<td class=K67>Q67</td>
<tr>
<td class=K71>Q71</td>
<td class=K72>Q72</td>
<td class=K73>Q73</td>
<td class=K74>Q74</td>
<td class=K75>Q75</td>
<td class=K76>Q76</td>
<td class=K77>Q77</td>
<tr>
</table>
"""

# The CSS for puzzles
puzzleCSS = """
body { font-family: Caulixtla008; }
.p7p {
        font-family: Caulixtla008;
        font-size: 24px;
        margin: 0;
        padding: 0;
        border-collapse: collapse;
        page-break-inside: avoid;
}
.p7p table {
        font-family: Caulixtla008;
        font-size: 24px;
        margin: 0;
        padding: 0;
        border-collapse: collapse;
}
.p7p td {
        padding: .9em;
}
.p7p td table td {
        width: 1em;
        height: 1em;
        padding: .1em;
        padding-left: .2em;
        padding-right: .2em;
        border-collapse: collapse;
        text-align: center;
}
.s0XX0  {
        border-left: 1px solid black;
        border-top: 1px solid black;
}
.s0XX1  {
        border-left: 3px solid black;
        border-top: 1px solid black;
}
.s1XX0  {
        border-left: 1px solid black;
        border-top: 3px solid black;
}
.s1XX1 {
        border-left: 3px solid black;
        border-top: 3px solid black;
}
.s0X10  {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
}
.s0X11  {
        border-left: 3px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
}
.s1X10  {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
}
.s1X11 {
        border-left: 3px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
}
.s01X0  {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-bottom: 3px solid black;
}
.s01X1  {
        border-left: 3px solid black;
        border-top: 1px solid black;
        border-bottom: 3px solid black;
}
.s11X0  {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-bottom: 3px solid black;
}
.s11X1 {
        border-left: 3px solid black;
        border-top: 3px solid black;
        border-bottom: 3px solid black;
}
.s0110  {
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
}
.s0111  {
        border-left: 3px solid black;
        border-top: 1px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
}
.s1110  {
        border-left: 1px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
}
.s1111 {
        border-left: 3px solid black;
        border-top: 3px solid black;
        border-right: 3px solid black;
        border-bottom: 3px solid black;
}
"""

allSeen = {}
# Here, 0 means "blank space"
if len(sys.argv) <= 2:
        puzzleQuestion = [[6,0,4,0,2,0,3,0,5,0,0,0,1,0,1,0,0,2,0,0,4,0,0,7,0,
                6,0,0,4,0,0,5,0,0,2,0,1,0,0,0,6,0,3,0,5,0,1,0,7]]
        polyominoPattern = [
            [1,1,1,2,3,3,3,
             1,1,1,2,4,3,3,
             1,2,2,2,4,3,3,
             2,2,4,4,4,5,5,
             6,6,4,5,5,5,7,
             6,6,4,5,7,7,7,
             6,6,6,5,7,7,7]]
             
else:
        puzzleQuestion = []
        polyominoPattern = []
        for index in range(2,len(sys.argv)):
                f = open(sys.argv[index])
                try:
                        i = f.read()
                except:
                        i = "Broken"
                # Grab question to print
                q = re.split('\n+',i)
                try:
                        q = s = g = q[1]
                except:
                        q = s = g = "Broken"
                q = re.sub('.*question difficult[^>]*>','',q)
                q = re.sub('</question.*','',q)

                # Grab answer to make sure we do not have dup puzzles
                s = re.sub('^.*<answer>','',s)
                s = re.sub('</answer.*$','',s)
                s = re.sub(' ','',s)
                s = normString(s)
                upsideDownS = normString(s[::-1])

                # Grab block arrangement ("group") to make sure we are
                # using the right one
                g = re.sub('</group.*','',g);
                g = re.sub('^.*<group[^>]*>','',g);
                pattern = re.split(' ',g)
                g = re.sub(' ','',g)
                g = normString(g)
                upsideDownG = normString(g[::-1])

                z = re.split(' ',q)
                usePuzzle = True
                if(len(g) != 49):
                        print("Puzzle " + sys.argv[index] + " is not 7x7")
                        usePuzzle = False
                if (s + "-" + g) in allSeen.keys():
                        print("Puzzle " + sys.argv[index] + " already seen in "
                    + allSeen[(s + "-" + g)])
                        if not dupCheckOnly:
                                print("Skipping")
                        usePuzzle = False
                        dupsFound = True
                # Let's see if, when we turn the puzzle upside down (180 
                # degree rotation), if it's the same as another puzzle
                if (upsideDownS + "-" + upsideDownG) in allSeen.keys():
                        print("Puzzle " + sys.argv[index] + " is inverse of "
                    + allSeen[(upsideDownS + "-" + upsideDownG)])
                        if not dupCheckOnly:
                                print("Skipping")
                        usePuzzle = False
                        dupsFound = True
                else:
                        allSeen[(s + "-" + g)] = sys.argv[index]
                if usePuzzle:
                        puzzleQuestion.append(z)
                        polyominoPattern.append(pattern)

allHTML = ""
pageNum = 1
for puzzle in range(len(puzzleQuestion)):
        if (puzzle % 6) == 0:
                allHTML += "<div class=p7p><table><tr><td>"
        index = 0
        puzzleHTML = puzzleTemplate
        for column in range(1,8):
                for row in range(1,8):
                        # Determine which pattern to give this puzzle
                        north = '1'
                        south = 'X'
                        east = 'X'
                        west = '1'
                        if index % 7 == 6:
                            east = '1'
                        if index > 41:
                            south = '1'
                        thisPattern = polyominoPattern[puzzle][index]
                        # Do we make the line on the left thick or thin?
                        leftPattern = -1
                        if index % 7 != 0:
                            leftPattern = polyominoPattern[puzzle][index - 1]
                        if thisPattern == leftPattern:
                            west = '0'
                        # Do we make the line on the top thick or thin?
                        upPattern = -1
                        if index > 6:
                            upPattern = polyominoPattern[puzzle][index - 7]
                        if thisPattern == upPattern:
                            north = '0'
                        replace = "Q" + str(column) + str(row)
                        thisNumber = puzzleQuestion[puzzle][index]
                        if int(thisNumber) == 0:
                                thisNumber = "&nbsp;"
                        puzzleHTML = re.sub(replace,str(thisNumber),puzzleHTML)
                        thisClass = 's' + north + south + east + west
                        replace = "K" + str(column) + str(row)
                        puzzleHTML = re.sub(replace,thisClass,puzzleHTML)
                        index += 1
        allHTML += puzzleHTML
        if (puzzle % 2) == 0:
                allHTML += "</td><td>"
        else: # Line break every other puzzle
                allHTML += "</td></tr><tr><td>"
        if (puzzle % 6) == 5: # Page break after six puzzles
                allHTML += "</td></tr></table></div>"
                allHTML += title + " &mdash; Page " + str(pageNum)
                pageNum += 1

if (puzzle % 6) != 5:
        allHTML += "</td></tr></table></div>"
        allHTML += "Page " + str(pageNum)

if dupCheckOnly:
    print("Dup check performed")
    if not dupsFound:
            print("No duplicate puzzles found")
    sys.exit(1)

html = HTML(string=allHTML)
css = CSS(string=puzzleCSS, font_config = font_config)
html.write_pdf(outputFile, stylesheets=[css], font_config=font_config)

print(outputFile + " written")
