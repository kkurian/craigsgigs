import peewee


class DatabaseFactory:
    @staticmethod
    def build(db_class, db_environment):
        if db_class == peewee.SqliteDatabase:
            db_name = 'db/{}.db'.format(db_environment)
        else:
            raise NotImplementedError
        return db_class(db_name)
