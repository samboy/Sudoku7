#!/usr/bin/env python

# This uses the version of Python included with CentOS 7 (Python2)

import sys, re
from weasyprint import HTML, CSS
from weasyprint.fonts import FontConfiguration

font_config = FontConfiguration()

# The HTML used to make puzzles

puzzleTemplate = """<div class=p7p>
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
</div>"""

# The CSS for puzzles
puzzleCSS = """@font-face {
    font-family: 'Caulixtla';
    src: url('Caulixtla008.woff')
         format('woff');
}
body { font-family: Caulixtla; }
.p7p table {
	font-family: Caulixtla;
        font-size: x-large;
        margin: 0;
        padding: 0;
        border-collapse: collapse;
}
.p7p td {
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

# For this version, we just use a hard-coded puzzle.  
# Here, 0 means "blank space"
puzzleQuestion = [6,0,4,0,2,0,3,0,5,0,0,0,1,0,1,0,0,2,0,0,4,0,0,7,0,6,0,0,4,
		0,0,5,0,0,2,0,1,0,0,0,6,0,3,0,5,0,1,0,7]

index = 0
puzzleHTML = puzzleTemplate
for column in range(1,8):
	for row in range(1,8):
		replace = "Q" + str(column) + str(row)	
		if puzzleQuestion[index] == 0:
			puzzleQuestion[index] = "&nbsp;"
		puzzleHTML = re.sub(replace, str(puzzleQuestion[index]),
				puzzleHTML)
		index += 1

html = HTML(string=puzzleHTML)
css = CSS(string=puzzleCSS, font_config = font_config)
html.write_pdf('Sudoku7.pdf', stylesheets=[css], font_config=font_config)

print "Sudoku7.pdf written"
