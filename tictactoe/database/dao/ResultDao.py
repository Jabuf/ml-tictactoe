import numpy as np

from tictactoe.constants.TicTacToeConstants import *
from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.entity.Session import Session


class ResultDao(ObjectDao):

    @staticmethod
    def get_all_results_by_game_states(game_state, results=None):
        if results is not None:
            return list(filter(lambda x: x.game_state == game_state, results))
        else:
            results = []
            for session in Session.objects:
                results += list(filter(lambda x: x.game_state == game_state, session.results))
        return results

    @staticmethod
    def get_results_by_sessions(sessions):
        if sessions is not None:
            results = []
            for session in sessions:
                results += session.results
            return results
        else:
            return []

    RBGS = get_all_results_by_game_states
    RBS = get_results_by_sessions

    @staticmethod
    def get_results_by_sessions_game_states(sessions, game_state):
        return ResultDao.RBGS(game_state, ResultDao.RBS(sessions))

    @staticmethod
    def get_stats(results):
        game_states = np.zeros(shape=(4, 2))
        for value in GAME_STATES.values():
            game_states[value][0] = value
        for result in results:
            game_states[result.game_state][1] += 1

        return game_states
