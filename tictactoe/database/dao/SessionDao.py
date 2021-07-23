from tictactoe.database.dao.ObjectDao import ObjectDao
from tictactoe.database.dao.ResultDao import ResultDao
from tictactoe.database.entity.Session import Session


class SessionDao(ObjectDao):

    @staticmethod
    def get_sessions_by_training_iteration(training_iteration=None):
        if training_iteration is not None:
            return Session.objects(training_iteration=training_iteration)
        else:
            return Session.objects

    @staticmethod
    def get_stats(sessions=None):
        if sessions is None:
            sessions = Session.objects
        stats = []

        for session in sessions:
            stats.append([session.training_iteration, ResultDao.get_stats(session.results)])
        return stats
