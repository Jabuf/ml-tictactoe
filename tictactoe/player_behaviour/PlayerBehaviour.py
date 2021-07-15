from locals import *


def get_player_move(board, turn):
    if not turn % 2 == 0:
        return __random_behaviour__(board, 2)
    else:
        return __random_behaviour__(board, 1)


def __random_behaviour__(board, player):
    while True:
        line = randint(0, 2)
        column = randint(0, 2)
        if board[line, column] == 0:
            board[line, column] = player
            return board
