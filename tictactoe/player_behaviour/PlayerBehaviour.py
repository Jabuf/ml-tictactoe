from random import randint

from tictactoe.constants.TicTacToeConstants import *


def get_player_move(board, player):
    return __random_behaviour__(board, player)


def check_player(turn):
    if turn % 2 == 0:
        return PLAYER1
    else:
        return PLAYER2


def __random_behaviour__(board, player):
    while True:
        line = randint(0, 2)
        column = randint(0, 2)
        if board[line, column] == 0:
            board[line, column] = player
            return [line, column]
