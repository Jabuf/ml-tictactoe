from mongoengine import *
from datetime import datetime


class EmbeddedEntity(EmbeddedDocument):
    meta = {'abstract': True}
    date = DateTimeField(default=datetime.today())
    pass
