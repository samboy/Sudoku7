# Sudoku7

Back in 2011, I found an open source Sudoku generator that can generate
any size of Sudoku, with any pattern for the subgrids.

I used the generator to make a handful of 7x7 Sudoku-like puzzles for
my blog.

Recently, I took an interest in this, and used the Java client to make
a seven-page, 42 puzzle Sudoku book.  The process was laborious: I used
the Java program to make a puzzle, then I had to put multiple screenshots
in an image for each page of the book using Gimp.  It took me about two
days to make a seven page book.

The purpose of this project is to make the entire process of making a
7x7 Sudoku puzzle easier.

# To play

Open up the file example.pdf.

This puzzle is a variant of Sudoku I like to call "Prosperity 7".  In
this Sudoku variant, the board is only 7x7, and only the numbers
from 1 to 7 are used.  Neither 8 nor 9 are ever placed on this
board.

The object of this puzzle is to place the numbers 1 through 7 in the
blank spaces such that:

* Each row only has one instance of each number between 1 and 7.  In
  other words, no number is duplicated in a given row.

* Each column only has one instance of each number between 1 and 7.  In
  other words, no number is duplicated in a given column.

* Each of the seven-square shapes bordered by thick lines have all
  of the numbers between 1 and 7 precisely once.  

The puzzles in example.pdf are sorted by difficulty, starting
with easier puzzles and moving up to hard puzzles.

# To generate PDF files

Have Python (either Python2 or Python3; the script is a polyglot) installed.  
Ideally, use a virtual environment.  Then:

```
pip install -r requirements.txt
./genPdf.py puzzle.pdf puzzles/*.xml 
```

Of course, one does not simply run `pip install -r requirements.txt` and
have everything work without problem.  There are various development 
libraries which need to be installed, but they are standard libraries
available for the system with both Cygwin and CentOS 7; the libraries 
that need to be installed include cairo, pixman, png, pango, and 
poppler.

The first argument for the `genPdf.py` script is the PDF file generated.

The subsequent arguments are files which are generated by the Java
program in the `Generator/` directory (to get one started, I have 
included a number of already generated puzzles in the `puzzles/`
directory).

It is also possible to use the script to only look for duplicate puzzles:

```
./genPdf.py dupcheck puzzles/*.xml
```

# Generating more puzzles

To generate more puzzles, we need a Java interpreter.  Both Oracle
Java 8 and OpenJDK 1.8.0_191 (i.e. the OpenJDK included with CentOS 7)
work with the supplied jar file which generates the puzzles in batch 
mode.

To run the puzzle generator, make sure to be in a GUI environment (X
windows, Windows 10, etc.) and run the following commands:

```
cd Generator/
./generatePuzzles.sh
```

This will run the Java generator in batch mode.  It will take about a 
minute to generate 18 puzzles.

# Generating puzzles by hand

In a GUI environment with Java installed, double clicking on the
`Sudoku-NPGeneratorV2_0_2.jar` file in the `Generator/` directory
should open up a generator.  With a command line, it would be:

```
cd Generator/
java -jar Sudoku-NPGeneratorV2_0_2.jar
```

At this point a GUI window will open with the Sudoku generator.
Do the following to generate a puzzle:

* Select File -> Open File
* Open the file `Prosperity-7-template.xml`
* Click on the button `Set` near the bottom of the window
* Click on the button `Generate`
* Click on the button `Play`
* Select File -> Save file
* Choose a unique filename for the file
* Click on `Save`

To the right of the button `Answer`, it shows how hard the puzzle is
(the more "points" a puzzle has, the harder it is to solve)

It's possible to change where we put number hints (one can observe a number
of different patterns for hints in the example.pdf file supplied 
here):  After opening up the `Prosperity-7-template.xml` file, click on `Set`
then right click to add or remove blue squares (squares were we put
number clues in a puzzle).

Note that in order to print, the puzzle `.xml` files need to be 7x7 files
using the same block arrangement (same set of heptominoes used the generate
the 7x7 square).  The PDF generator can handle different location for the
number hints; it can *not* handle a different arrangement of sub-blocks
nor a different puzzle size (the PDF generator will refuse to print 
incompatible files).

# Installing the Caulixtla008 font

While the puzzles look perfectly fine using the Weasyprint
default font, one can optionally install the Caulixtla008.woff
font.  See this page for notes:

>https://weasyprint.readthedocs.io/en/latest/features.html#fonts

Example #1 (Windows + Cygwin, should work elsewhere):

```
mkdir ~/.fonts
cp Caulixtla008.woff ~/.fonts
```

Example #2 (CentOS 7 system-level install):

```
mkdir /usr/share/fonts/Caulixtla008
cp Caulixtla008.woff /usr/share/fonts/Caulixtla008/
fc-cache
```
