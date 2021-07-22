import abc

from tictactoe.database.entity.Entity import Entity


class ObjectDao(abc.ABC):

    @staticmethod
    def clear_database():
        for child in Entity.__subclasses__():
            child.objects.delete()
