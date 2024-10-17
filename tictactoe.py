"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    countEMPTY = 0
    for row in board:
        for element in row:
            if element == "X":
                countX += 1
            elif element == "O":
                countO += 1
            else:
                countEMPTY += 1
    
    if countEMPTY == 9:
        return "X"
    elif countX > countO:
        return "O"
    else:
        return "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    availableSpots = set()
    for i, row in enumerate(board):
        for j, element in enumerate(row):
            if element == EMPTY:
                availableSpots.add((i, j))
    return availableSpots


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j= action
    if action in actions(board):
        newBoard = copy.deepcopy(board)
        newBoard[i][j] = player(board)
        return newBoard
    else:
        raise NameError("Not Valid Move")

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Check Rows
    for row in board:
        if row == ["X" , "X", "X"]:
            return "X"
        elif row == ["O", "O", "O"]:
            return "O"
   #Check Diagonials         
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    elif board[0][2] == board[1][1] == board [2][0] != EMPTY:
        return board[0][2]
    #Check Columns
    if board[0][0] == board[1][0] == board[2][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] != EMPTY:
        return board[0][2]
    #No winner yet
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None:
        return True
    else:
        for i, row in enumerate(board):
            for j, element in enumerate(row):
                if element == EMPTY: 
                    return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    turn = player(board)
    if terminal(board):
        return None
    if turn == "X":
        bestValue = -100
        bestMove = None
        for move in actions(board):
            value = MinValue(result(board, move))
            if value > bestValue:
                bestValue = value
                bestMove = move
    else:
        bestValue = 100
        bestMove = None
        for move in actions(board):
            value = MaxValue(result(board, move))
            if value < bestValue:
                bestValue = value
                bestMove = move
    return bestMove
        
        

def MaxValue(board):
    if terminal(board):
        return utility(board)
    v = -100
    moves = actions(board)
    for move in moves:
        v = max(v, MinValue(result(board, move)))
    return v

def MinValue(board):
    if terminal(board):
        return utility(board)
    v = 100
    moves = actions(board)
    for move in moves:
        v = min(v, MaxValue(result(board, move)))
    return v