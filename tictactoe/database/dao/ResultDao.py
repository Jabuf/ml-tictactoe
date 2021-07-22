import numpy as np

from tictactoe.constants.TicTacToeConstants import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.entity.Result import Result


class ResultDao(ObjectDao):

    @staticmethod
    def get_stats_game_states(datetime=None):
        game_states = np.zeros(shape=(4, 2))
        for value in GAME_STATES.values():
            game_states[value][0] = value
        for result in Result.objects:
            if datetime is None or result.date > datetime:
                game_states[result.game_state][1] += 1

        return game_states

    @staticmethod
    def get_results_by_game_states(game_state):
        return Result.objects(game_state=game_state)
