from datetime import datetime

from bson.objectid import ObjectId
from mongoengine import *


class Entity(Document):
    meta = {'abstract': True}
    id = ObjectId()
    date = DateTimeField(default=datetime.today())
    pass
