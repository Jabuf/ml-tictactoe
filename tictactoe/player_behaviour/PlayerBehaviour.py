from tictactoe.ml.Prediction import *


def get_player_move(board, results=None, opp_move=None, turn=None):
    """
    Get the next move to make
    @param board: board of the current game
    @param results: successful data from previous games
    @param opp_move: move make by the opponent
    @param turn: current turn
    @return: a valid move
    """
    if results is not None:
        return __trained_behaviour__(board, results, opp_move, turn)
    else:
        return __random_behaviour__(board)


def __trained_behaviour__(board, results, opp_move, turn):
    """
    Make a random move among successful valid moves from previous games
    @param board: board of the current game
    @param opp_move: move make by the opponent
    @param results: successful data from previous games
    @return: a random move among successful valid moves from previous games if there's one, otherwise a random move
    """
    move = get_next_move(results, opp_move, board, turn)
    if move is not None:
        return move
    else:
        return __random_behaviour__(board)


def __random_behaviour__(board):
    """
    Make a random valid move
    @param board: board of the current game
    @return: a valid move
    """
    while True:
        line = randint(0, 2)
        column = randint(0, 2)
        if board[line, column] == 0:
            return [line, column]
