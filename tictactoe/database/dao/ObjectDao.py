import abc
from abc import abstractmethod
from tictactoe.database.entity.Entity import Entity
from typing import TypeVar, Generic


class ObjectDao(abc.ABC):

    @staticmethod
    @abstractmethod
    def delete_all():
        pass
