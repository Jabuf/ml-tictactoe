from mongoengine import *
from tictactoe.database.entity.Entity import Entity
from tictactoe.database.entity.Turn import Turn


class Result(Entity):
    game_state = IntField()
    turns = EmbeddedDocumentListField(Turn)
