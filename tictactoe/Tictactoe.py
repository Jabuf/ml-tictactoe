from locals import *
from tictactoe.player_behaviour.PlayerBehaviour import get_player_move

# game states
IN_PROGRESS = 0
PLAYER1_WON = 1
PLAYER2_WON = 2
DRAW = 3


def __init_ttt_board__():
    ttt_board = array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    return ttt_board


def play_game_ttt():
    board = __init_ttt_board__()
    game_state = 0
    turn = 0
    while not game_state > 0 and turn < 9:
        board = __play_round_ttt__(board, __check_player__(turn))
        game_state = __check_victory__(board)
        turn += 1

    if turn == 8 and game_state == 0:
        game_state = 3

    return [game_state, board]


def __play_round_ttt__(board, player):
    return get_player_move(board, player)


def __check_victory__(board):
    game_state = __check_lines__(board)
    # check columns
    if game_state == 0:
        game_state = __check_lines__(transpose(board))
    if game_state == 0:
        game_state = __check_diagonals__(board)

    return game_state


def __check_lines__(board):
    game_state = 0
    for i in range(0, 2):
        if board[i, 0] == board[i, 1] and board[i, 0] == board[i, 2]:
            return board[i, 0]
    return game_state


def __check_diagonals__(board):
    game_state = 0
    for i in range(0, 2):
        if board[0, 0] == board[1, 1] and board[0, 0] == board[2, 2]:
            return board[0, 0]
        if board[0, 2] == board[1, 1] and board[0, 2] == board[2, 0]:
            return board[0, 2]
    return game_state


def __check_player__(turn):
    if turn % 2 == 0:
        return 1
    else:
        return 2
