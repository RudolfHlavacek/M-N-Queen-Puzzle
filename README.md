# M-N-Queen-Puzzle
An Eight Queen Puzzle enhanced by option to create board with M x N fields

Script m_n_queen_puzzle.py finds solutions for Eight Queen Puzzle.
However it is modified version of this problem.
It can find solutions for non-specific chess boards.

Before it starts solving the puzzle, the script asks User for few input parameters.
INPUTS from user:
        - M - number of rows
        - N - number of columns
        - If user is satisfied with only first solution or if it is required to find all solutions.
        - If user want to display every iteration or not.
            (This option really really REALLY slows down whole algorithm!!!)
OUTPUT:
        - It prints one or every solution on the screen. (Depends on user's choice.)
        - If there is at least one solution then user is asked if wants to print specific solution.
            - If not the he can terminate script by entering 'Q'.

Author: Rudolf Hlaváček
Date: 12.08.2020
Version: 1.0.0
Python version: 3.7.6
Python enviroment:
Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] :: Anaconda, Inc. on win32
