from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity
from tictactoe.database.entity.Turn import Turn


class Result(EmbeddedEntity):
    game_state = IntField()
    turns = EmbeddedDocumentListField(Turn)
