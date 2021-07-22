from datetime import datetime

from mongoengine import *


class EmbeddedEntity(EmbeddedDocument):
    meta = {'abstract': True}
    date = DateTimeField(default=datetime.today())
    pass
