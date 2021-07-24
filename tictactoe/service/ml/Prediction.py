from collections import Counter
from random import randint

# from tictactoe.service.MoveService import get_all_possible_moves


def get_next_move(results, move, board, turn):
    """
    Choose a random move among successful valid moves from previous games
    @param results: successful data from previous games
    @param move: move make by the opponent
    @param board: board of the current game
    @param turn: current turn
    @return: a move
    """
    moves = get_successful_moves(results, move, turn)
    get_valid_moves(board, moves)
    # return get_most_played_move(moves)

    if len(moves) > 1:
        return moves[randint(0, len(moves) - 1)]
    else:
        return None


def get_successful_moves(results, move, turn_number):
    """
    Return all the moves made against the move passed in parameter during a winning game
    @param results: winning games
    @param move: move made by the opponent
    @param turn_number: current turn
    @return: list of moves
    """
    moves = []
    for result in results:
        if turn_number == 0:
            moves += [x.move for x in (list(filter(lambda x: x.number == 0, result.turns)))]
        else:
            for turn in result.turns:
                if turn.number == turn_number - 1 and turn.move.equals(move):
                    moves += [x.move for x in (list(filter(lambda x: x.number == turn_number, result.turns)))]

    return moves


def get_valid_moves(board, moves):
    """
    Return the moves that can be played on the board
    @param board: board of the current game
    @param moves: a list of moves
    @return: moves that are valid
    """
    for move in moves:
        if not board[move.line, move.column] == 0:
            moves.remove(move)

    return moves


def get_most_played_move(moves):
    """
    Return the move played move among a list
    @param moves: a list of moves
    @return: most played move
    """
    # get_a
    move = Counter(moves).most_common(1)

    return move
