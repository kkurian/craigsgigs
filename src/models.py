import datetime

import peewee

from .models_base import ModelsBase


class Models(ModelsBase):
    def __init__(self, database):
        self._posting = None
        super().__init__(database, ['Posting'])

    @property
    def Posting(self):  # NOQA
        if self._posting is None:
            class Posting(self.BaseModel):
                posted_at = peewee.DateTimeField()
                text = peewee.TextField()
                url = peewee.TextField()
                created_at = peewee.DateTimeField(default=datetime.datetime.utcnow())  # NOQA
                updated_at = peewee.DateTimeField(default=datetime.datetime.utcnow())  # NOQA
            self._posting = Posting
        return self._posting
