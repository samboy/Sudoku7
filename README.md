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

# To use

Have Python installed.  Ideally, use a virtual environment.  Then:

```
pip install -r requirements.txt
./genPdf.py puzzle.pdf puzzles/Prosperity-7-0107pt.xml \
	puzzles/Prosperity-7-0108pt.xml \
	puzzles/Prosperity-7-0116pt.xml \
	puzzles/Prosperity-7-0121pt.xml \
	puzzles/Prosperity-7-0122pt.xml \
	puzzles/Prosperity-7-0141pt.xml
```

The first argument is the PDF file generated.
The subsequent arguments are files which are generated by the Java
program in the `Generator/` directory.

Note that the puzzle `.xml` files need to be ones generated using the
supplied `Generator/Prosperity-7-template.xml` file (actually, the 
generator can handle different location for the number hints; it can
*not* handle a different arrangement of sub-blocks nor a different
puzzle size).

