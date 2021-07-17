from mongoengine import *


class Result(Document):
    result = int
    number_turn = int
