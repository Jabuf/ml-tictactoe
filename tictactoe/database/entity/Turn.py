from mongoengine import *

from tictactoe.database.entity.EmbeddedEntity import EmbeddedEntity
from tictactoe.database.entity.Move import Move


class Turn(EmbeddedEntity):
    number = IntField()
    move = EmbeddedDocumentField(Move)
    player = IntField()
