from mongoengine import *

from tictactoe.database.entity.Entity import Entity
from tictactoe.database.entity.Result import Result


class Session(Entity):
    training_iteration = IntField()
    results = EmbeddedDocumentListField(Result)
