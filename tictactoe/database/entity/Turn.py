from mongoengine import *

from tictactoe.database.entity.Entity import Entity


class Turn(Entity):
    turn = IntField()
    move = ListField(IntField())
    player = IntField()
    # result = Result
