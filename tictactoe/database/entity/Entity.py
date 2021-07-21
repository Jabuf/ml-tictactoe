from mongoengine import *
from bson.objectid import ObjectId
from datetime import datetime


class Entity(Document):
    meta = {'abstract': True}
    id = ObjectId()
    date = DateTimeField(default=datetime.today())
    pass
