from mongoengine import *


class Entity(Document):
    meta = {'abstract': True}
    id = IntField()
    pass
