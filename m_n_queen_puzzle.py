'''
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
'''

from copy import deepcopy
import os
import numpy as np




def _get_empty_line(n, spacer=' ', border_char='|'):
    '''
    Function is used for creation of chess board lines.
    Returns formated string with specific combinations of input characters.
    INPUTS: n - number of chess board columns
            spacer - with this character is filled empty field for queen.
            border_char - this character separates different spacer groups.

    OUTPUT: returns formated string

    E.g. _get_empty_line(3)              returns '|   |   |   |'
    E.g. _get_empty_line(3, '-', '+')    returns '+---+---+---+'
    E.g. _get_empty_line(4, '-', '+')    returns '+---+---+---+---+'
    '''
    return f'{spacer*3}'.join([border_char for x in range(n+1)])


def _put_queen_on_the_line(queen_position, line):
    '''
    Function place 'Q' for Queen into the string representing one row of the chess board.
    INPUTS: queen_position - column position of the queen
            line - string where shall be inserted 'Q'.
    OUTPUT: returns formated string

    E.g. _put_queen_on_the_line(0, '|   |   |   |')     returns '| Q |   |   |'
    E.g. _put_queen_on_the_line(1, '|   |   |   |')     returns '|   | Q |   |'
    E.g. _put_queen_on_the_line(1, '|   |   |   |   |') returns '|   | Q |   |   |'
    '''
    pos_adj = 4*queen_position + 2
    return line[:pos_adj] + 'Q' + line[pos_adj+1:]


def print_board(board):
    '''
    Function print on the screen chess board.
    INPUT: board - numpy.array object representing chess board.
                    - Value 1 in array means there is queen on position.
                    - Value 0 in array means there is no queen.
    '''
    m, n = board.shape
    print('     ' + _get_empty_line(n, '-', '+'))

    for r in range(m):
        new_line = _get_empty_line(n)
        for c in range(n):
            if board[r][c] == 1:
                new_line = _put_queen_on_the_line(c, new_line)
        new_line = f' {m-r:>3} ' + new_line
        print(new_line)
        print('     ' + _get_empty_line(n, '-', '+'))

    print('       ' + '   '.join([chr(num+ord('a')) for num in range(n)]))


def clear():
    '''
    Function clears Command Line Interface.
    '''
    os.system('cls')

def is_possible(board, pos):
    '''
    Function checks if queen can be placed on position pos.
    INPUTS: board - numpy.array object representing chess board.
                    - Value 1 in array means there is queen on position.
                    - Value 0 in array means there is no queen.
            pos - Tested position in tuple form.
                    - E.g. (3, 4) means 3rd row and 4th column. Numbering starts from 0.

    OUTPUT: Returns True if it is safe to place queen on position. If not then returns False.
    '''
    m, n = board.shape
    r, c = pos
    # Check in column
    for i in range(m):
        if board[i][c] == 1:
            return False
    # Check in row
    for i in range(n):
        if board[r][i] == 1:
            return False
    # Check in diagonals
    # Getting upper left starting point
    r_0 = r
    c_0 = c
    while (r_0 != 0) and (c_0 != 0):
        r_0 -= 1
        c_0 -= 1
    # Checking to right and down
    while (r_0 != m) and (c_0 != n):
        if board[r_0][c_0] == 1:
            return False
        r_0 += 1
        c_0 += 1

    # Getting upper right starting point
    r_0 = r
    c_0 = c
    while (r_0 != 0) and (c_0 != n-1):
        r_0 -= 1
        c_0 += 1
    # Checking to left and down
    while (r_0 != m) and (c_0 != -1):
        if board[r_0][c_0] == 1:
            return False
        r_0 += 1
        c_0 -= 1

    return True


COUNTER = 0
def solve(m, n, board, start_row, list_of_solutions, first_solution=False, display=True):
    '''
    Function solves M x N Queen Puzzle.
    INPUTS: - m - Number of chess board rows.
            - n - Number of chess board columns.
            - board - numpy.array object with dimension M x N.
                    - Represents chess board.
                    - Element with value 0 means there is no queen.
                    - Element with value 1 means there is queen.
            - start_row - Used during recursion.
                        - If is function run for the first time set to 0.
            - list_of_solutions - list containing all founded solutions.
            - first_solution    - If True then script will find ONLY ONE solution.
                                - Otherwise all solutions will be found.
            - dislay - If set to True then script displays on the screen every step.
                        - It significantly increase amount of time!!!
    OUTPUT: - list_of_solutions - In this passed in user finds solution(s).
                                - Every solution is deepcopied to the list of numpy.array objects.
    '''
    global COUNTER
    if COUNTER >= 1 and first_solution:
        return

    if start_row >= m:
        COUNTER += 1
        list_of_solutions.append(deepcopy(board))
        return


    for col in range(n):
        if is_possible(board, (start_row, col)):
            board[start_row][col] = 1

            if display:
                clear()
                print(f'Solutions found: {COUNTER}')
                print_board(board)

            solve(m, n, board, start_row+1, list_of_solutions, first_solution, display)
            board[start_row][col] = 0

            if display:
                clear()
                print(f'Solutions found: {COUNTER}')
                print_board(board)

def print_all_sol(list_of_solutions):
    '''
    From passed-in list of numpy.array objects it will print on screen every single solution.
    '''
    if len(list_of_solutions) > 0:
        for i, item in enumerate(list_of_solutions):
            print(f'Solution #{i+1}')
            print_board(item)
            print()
        print(f'Solutions found: {len(list_of_solutions)}')
    else:
        print('SORRY. No solutions found. :(')



if __name__ == '__main__':
##################### Getting dimensions of the chess board ####################
    while True:
        try:
            M = int(input('Choose number of rows for board: M = '))
            N = int(input('Choose number of columns for board: N = '))
            if M <= 0 or N <= 0:
                raise ValueError
            break
        except ValueError:
            print('ONLY positive integer value is allowed!\n')
##################### Getting dimensions of the chess board ####################

###################### Only ONE solution or ALL solutions ######################
    choice = ''
    while choice.upper() not in ['YES', 'Y', 'NO', 'N']:
        choice = input('Do you want to have all solutions? (Y / N): ')
    if choice.upper() in ['YES', 'Y']:
        ONLY_FIRST_SOLUTION = False
    else:
        ONLY_FIRST_SOLUTION = True
        print('Script will stop after first solution is found.')
###################### Only ONE solution or ALL solutions ######################

######################## Asks for displaying every step ########################
    choice = ''
    while choice.upper() not in ['YES', 'Y', 'NO', 'N']:
        choice = input('Do you want to see how script will solve this puzzle '\
                        +'(It is much more slower!)? (Y / N): ')
    DISPLAY = choice.upper() in ['YES', 'Y']
######################## Asks for displaying every step ########################

    # If M is bigger than N then swap these dimensions.
    # Because algorithm cannot solve cases with more rows then columns.
    # Because of this it is also necessary to transpose results.
    if M > N:
        M, N = N, M

        TRANSPOSE_RESULTS = True
    else:
        TRANSPOSE_RESULTS = False

    # Creating empty chess board and list of founded solutions.
    CHESS_BOARD = np.zeros((M, N), dtype='int8')
    SOLUTIONS = []


################### Aplying recursive algorithm to solve this ##################
    solve(M, N, CHESS_BOARD, 0, SOLUTIONS, first_solution=ONLY_FIRST_SOLUTION, display=DISPLAY)
################### Aplying recursive algorithm to solve this ##################

    # If M is bigger then N then it is necessary to transpose results.
    if TRANSPOSE_RESULTS:
        for i in range(len(SOLUTIONS)):
            SOLUTIONS[i] = deepcopy(SOLUTIONS[i].transpose())


    clear()
    print_all_sol(SOLUTIONS)


##################### Asks if show some results or to quit #####################
    choice = ''
    while choice.upper() not in ['Q', 'QUIT', 'EXIT']:
        length = len(SOLUTIONS)
        if length > 0:
            print('To display on the screen specific solution enter index number.')
        choice = input('If you want to quit enter <Q>: ')
        if length > 0:
            try:
                choice = int(choice)
                if 0 < choice < length+1:
                    print(f'Solution #{choice}')
                    print_board(SOLUTIONS[choice-1])
                    print()
                else:
                    print(f'Invalid index! Choose from 1 to {length}')

                choice = ''
            except ValueError:
                pass
##################### Asks if show some results or to quit #####################
