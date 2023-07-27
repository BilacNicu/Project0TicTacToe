"""
Tic Tac Toe Player
"""
import copy
import math

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
    countX = 0
    countO = 0

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == X:
                countX += 1
            if board[row][col] == O:
                countO +=1

    if countX > countO:
        return 0
    else:
        return X

def actions(board):
    allPossibleActions = set()

    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == EMPTY:
                allPossibleActions.add((row,col))

    return allPossibleActions

def result(board, action):

    if action not in actions(board):
        raise Exception("Not valid action")

    row, col = action
    board_copy = copy.deepcopy(board)
    board_copy[row][col] = player(board)
    return board_copy

def checkRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == board[row][2] == player:
            return True
    return False

def checkColumn(board, player):
    for col in range(len(board)):
        if board[col][0] == player and board[col][1] == board[col][2] == player:
            return True
    return False

def checkFirstDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def checkSecondDig(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if (len(board) - row - 1) == col and board[row][col] == player:
                count += 1
    if count == 3:
        return True
    else:
        return False

def winner(board):
    if checkRow(board, X) or checkColumn(board, X) or checkFirstDig(board, X) or checkSecondDig(board, X):
        return X
    if checkRow(board, O) or checkColumn(board, O) or checkFirstDig(board, O) or checkSecondDig(board, O):
        return O
    else:
        return None

def terminal(board):
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True

def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
def min_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
def minimax(board):
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board, action)),action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]

    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board, action)),action])
        return sorted(plays, key=lambda x: x[0])[0][1]
