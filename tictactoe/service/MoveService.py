class Move:

    @staticmethod
    def get_all_possible_moves():
        moves = []
        for line in range(0, 2):
            for column in range(0, 2):
                moves.append([line, column])
        return moves
