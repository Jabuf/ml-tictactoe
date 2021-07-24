from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity


class Move(EmbeddedEntity):
    column = IntField()
    line = IntField()


