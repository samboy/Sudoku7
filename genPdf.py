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

allSeen = {}
# Here, 0 means "blank space"
if len(sys.argv) <= 2:
        puzzleQuestion = [[6,0,4,0,2,0,3,0,5,0,0,0,1,0,1,0,0,2,0,0,4,0,0,7,0,
                6,0,0,4,0,0,5,0,0,2,0,1,0,0,0,6,0,3,0,5,0,1,0,7]]
else:
        puzzleQuestion = []
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
                g = re.sub(' ','',g)
                g = normString(g)

                z = re.split(' ',q)
                usePuzzle = True
                if g != '1112333111243312224332244455664555766457776665777':
                        print("Puzzle " + sys.argv[index] +
                                " has incompatible design")
                        print("Skipping")
                        usePuzzle = False
                if s in allSeen.keys():
                        print("Puzzle " + sys.argv[index] + " already seen in "
                    + allSeen[s])
                        if not dupCheckOnly:
                                print("Skipping")
                        usePuzzle = False
                        dupsFound = True
                # Since we have point symmetry with the heptomino pattern, 
                # rotated upside down puzzles are dups
                if upsideDownS in allSeen.keys():
                        print("Puzzle " + sys.argv[index] + " is inverse of "
                    + allSeen[upsideDownS])
                        if not dupCheckOnly:
                                print("Skipping")
                        usePuzzle = False
                        dupsFound = True
                else:
                        allSeen[s] = sys.argv[index]
                if usePuzzle:
                        puzzleQuestion.append(z)

allHTML = ""
pageNum = 1
for puzzle in range(len(puzzleQuestion)):
        if (puzzle % 6) == 0:
                allHTML += "<div class=p7p><table><tr><td>"
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
