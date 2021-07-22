from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity


class Turn(EmbeddedEntity):
    turn = IntField()
    move = ListField(IntField())
    player = IntField()
