import numpy as np

from tictactoe.constants.TicTacToeConstants import GAME_STATES
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.entity.Result import Result


class ResultDao(ObjectDao):

    @staticmethod
    def get_stats_game_states():
        game_states = np.zeros(shape=(4, 2))
        for value in GAME_STATES.values():
            game_states[value][0] = value
        for result in Result.objects:
            game_states[result.game_state][1] += 1

        return game_states
