"""
First attempt at a simple game. This is a very basic version of TTT currently, more rules are needed.
"""

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ', 'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

def printBoard(board):
    "Printing out the board as needed"
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
turn = 'X'

for i in range(9):
    printBoard(theBoard)
    move = input('Turn for ' + turn + '. Move on which space?')
    theBoard[move] = turn
    
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'