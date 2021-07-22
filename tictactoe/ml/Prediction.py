from random import randint


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
        for turn in result.turns:
            if turn_number == 0 or turn.number == turn_number - 1:
                if turn.move == move:
                    moves += [move]
    return moves


def get_valid_moves(board, moves):
    """
    Return the moves that can be played on the board
    @param board: board of the current game
    @param moves: a list of moves
    @return: moves that are valid
    """
    for move in moves:
        if not board[move[0], move[1]] == 0:
            moves.remove(move)

    return moves
