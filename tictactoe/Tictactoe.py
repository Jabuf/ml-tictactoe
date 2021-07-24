from datetime import datetime

import numpy as np
from numpy import transpose

from tictactoe.constants.TicTacToeConstants import *
from tictactoe.database.entity.Result import Result
from tictactoe.database.entity.Turn import Turn


def __init_ttt_board__():
    ttt_board = np.zeros(shape=(3, 3))
    return ttt_board


def play_game_ttt(session, results=None):
    board = __init_ttt_board__()
    result = Result(game_state=IN_PROGRESS, date=datetime.today())
    turn = 0
    last_move = [0, 0]

    while not result.game_state > IN_PROGRESS and turn < 9:
        # For now we train only the player 1
        if results is not None and check_player(turn) == PLAYER2:
            [board, last_move] = __play_round_ttt__(board, check_player(turn), result, turn, session, results,
                                                    last_move)
        else:
            board = __play_round_ttt__(board, check_player(turn), result, turn, session)[0]

        result.game_state = __check_victory__(board)
        turn += 1

    if turn == 9 and result.game_state == IN_PROGRESS:
        result.game_state = DRAW

    session.results.append(result)


def __play_round_ttt__(board, player, result, turn, session, results=None, opp_move=None):
    move = get_player_move(board, session, results, opp_move, turn)
    play_move(board, move, player)
    result.turns.append(Turn(number=turn, move=move, player=player, date=datetime.today()))
    return [board, move]


def __check_victory__(board):
    game_state = __check_lines__(board)
    if game_state == IN_PROGRESS:
        # check columns
        game_state = __check_lines__(transpose(board))
    if game_state == IN_PROGRESS:
        game_state = __check_diagonals__(board)

    return game_state


def __check_lines__(board):
    game_state = IN_PROGRESS
    for i in range(0, 2):
        if board[i, 0] == board[i, 1] and board[i, 0] == board[i, 2]:
            return board[i, 0]
    return game_state


def __check_diagonals__(board):
    game_state = IN_PROGRESS
    for i in range(0, 2):
        if board[0, 0] == board[1, 1] and board[0, 0] == board[2, 2]:
            return board[0, 0]
        if board[0, 2] == board[1, 1] and board[0, 2] == board[2, 0]:
            return board[0, 2]
    return game_state


def play_move(board, move, player):
    board[move.line, move.column] = player


def check_player(turn):
    if turn % 2 == 0:
        return PLAYER1
    else:
        return PLAYER2
