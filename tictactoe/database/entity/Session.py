from mongoengine import *

from tictactoe.database.entity.Entity import Entity
from tictactoe.database.entity.Result import Result


class Session(Entity):
    training_iteration = IntField(default=0)
    pool_successful_games = IntField(default=0)
    random_moves = IntField(default=0)
    predicted_moves = IntField(default=0)
    execution_time = FloatField(default=0)
    results = EmbeddedDocumentListField(Result)
