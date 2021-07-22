from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity


class Turn(EmbeddedEntity):
    number = IntField()
    move = ListField(IntField())
    player = IntField()
