import peewee


class DatabaseFactory:
    @staticmethod
    def build(db_class, db_environment):
        if db_class == peewee.SqliteDatabase:
            db_name = f'db/{db_environment}.db'
        else:
            raise NotImplementedError
        return db_class(db_name)
