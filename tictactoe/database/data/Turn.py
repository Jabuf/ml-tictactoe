from mongoengine import *


class Turn(Document):
    turn = IntField()
    move = ListField(IntField())
    player = IntField()
    # result = Result
