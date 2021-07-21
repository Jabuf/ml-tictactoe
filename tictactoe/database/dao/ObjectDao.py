import abc
from abc import abstractmethod
from tictactoe.database.entity.Entity import Entity


class ObjectDao(abc.ABC):

    @staticmethod
    @abstractmethod
    def delete_all():
        pass

    @staticmethod
    def clear_database():
        for child in Entity.__subclasses__():
            child.objects.delete()
