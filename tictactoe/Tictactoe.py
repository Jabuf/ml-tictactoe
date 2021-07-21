from locals import *
from tictactoe.database.entity.Turn import Turn
from tictactoe.database.entity.Result import Result
from tictactoe.player_behaviour.PlayerBehaviour import get_player_move
from constants.TicTacToeConstants import *


def __init_ttt_board__():
    ttt_board = array([[0, 0, 0], [0, 0, 0], [0, 0, 0]])
    return ttt_board


def play_game_ttt():
    board = __init_ttt_board__()
    result = Result(game_state=IN_PROGRESS)
    turn = 0

    while not result.game_state > IN_PROGRESS and turn < 9:
        board = __play_round_ttt__(board, __check_player__(turn), result, turn)
        result.game_state = __check_victory__(board)
        turn += 1

    if turn == 8 and result.game_state == IN_PROGRESS:
        result.game_state = DRAW

    result.save()
    return [result.game_state, board]


def __play_round_ttt__(board, player, result, turn):
    move = get_player_move(board, player)
    result.turns.append(Turn(turn=turn, move=move, player=player))
    return board


def __check_victory__(board):
    game_state = __check_lines__(board)
    # check columns
    if game_state == IN_PROGRESS:
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


def __check_player__(turn):
    if turn % 2 == 0:
        return PLAYER1
    else:
        return PLAYER2
