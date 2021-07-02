# 8-queens
Solving the 8-queens problem using the Genetic Algorithm

What is the 8-queens problem?

Imagine an 8x8 chess board and in every column you place one queen on a tile.
Is there such a way to orient the queens so that none of the queens are attacking
each other? Reminder, for those who don't play chess, a queen can move in any
direction (vertical, horizontal, and diagonal) on the chess board for as far as
they want (or until they hit a wall, or another game piece). To be under attack
means that at least two queens share a row, column, or diagonal.

Must have python available on your system in order to run.
To run the 8-queens program execute the python file named "eightQueens"
  
  python eightQueens.py

The intention of this code is to learn how to implement the Genetic Algorithm
in a fun and interesting way. This code is from an Artificial Intelligence
course, and I have been given permission to make this code public.

Once the program is ran a function will be call to start running a test. The test
will generate a random board and randomize the orientation of the "8 queens" as well
as populating the population Node, which keeps track of the board state and the different
orientations of the 8 queens.

I did not implement a way for the user to change the population or number
of iterations. The program will ask if the user wants to read how the 
program runs, if they do they need to enter "y" or "Y". If they'd rather
skip the instructions then they can hit the enter key. The program will
then run 5 tests automatically, and 1 at the user's discretion.
