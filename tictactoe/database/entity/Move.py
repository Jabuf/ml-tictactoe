from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity


class Move(EmbeddedEntity):
    line = IntField()
    column = IntField()

    def equals(self, move):
        return self.column == move.column and self.line == move.line
