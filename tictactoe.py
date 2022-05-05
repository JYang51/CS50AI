"""
Tic Tac Toe Player
"""

from json.encoder import INFINITY
import math
from copy import deepcopy

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
    roundsPlayed = 0
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] != EMPTY):
                roundsPlayed += 1
    if (roundsPlayed % 2 == 0):
        return X
    else: 
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = []
    for i in range(len(board)):
        for j in range(len(board)):
            if (board[i][j] == EMPTY):
                moves.append((i, j))
    return moves

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = deepcopy(board)
    newBoard[action[0]][action[1]] = player(board)
    return newBoard

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for row in range(3):
        if (checkRow(row, board) != EMPTY):
            return checkRow(row, board)
    for column in range(3):
        if (checkColumn(column, board) != EMPTY):
            return checkColumn(column, board)
    for diag in range(2):
        if (checkDiag(diag, board) != EMPTY):
            return checkDiag(diag, board)

def checkColumn(colNum, board):
    currentSymbol = board[0][colNum]
    for i in range(3):
        if (board[i][colNum] != currentSymbol):
            return EMPTY
    return currentSymbol

def checkRow(rowNum, board):
    currentSymbol = board[rowNum][0]
    for i in range(3):
        if (board[rowNum][i] != currentSymbol):
            return EMPTY
    return currentSymbol

def checkDiag(diagNum, board):
    symbol = board[1][1]
    whichDiag = 1 - (diagNum * 2)
    if (symbol != board[1 + whichDiag][2]):
        return EMPTY
    if (symbol != board[1 - whichDiag][0]):
        return EMPTY
    return symbol


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) != EMPTY):
        return True
    if (len(actions(board)) == 0):
        return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X):
        return 1
    if (winner(board) == O):
        return -1
    return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)
    """
    currentPlayer = player(board)
    bestMove = (0,0)
    possibleActions = actions(board)

    if (currentPlayer == X):   
        bestMoveUtil = -INFINITY
        for action in possibleActions:
            if (minVal(result(board, action)) > bestMoveUtil):
                bestMove = action
                bestMoveUtil = minVal(result(board, action))
        return bestMove
    elif (currentPlayer == O):   
        bestMoveUtil = INFINITY
        for action in possibleActions:
            if (maxVal(result(board, action)) < bestMoveUtil):
                bestMove = action
                bestMoveUtil = maxVal(result(board, action))
        return bestMove

def maxVal(board):
    v = -INFINITY
    if (terminal(board)):
        return utility(board)
    for action in actions(board):
        v = max(v, minVal(result(board,action)))
    return v
    
def minVal(board):
    v = INFINITY
    if (terminal(board)):
        return utility(board)
    for action in actions(board):
        v = min(v, maxVal(result(board,action)))
    return v