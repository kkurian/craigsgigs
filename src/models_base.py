import peewee


class ModelsBase:
    """Perform gymnastics to allow the database to be specified at runtime.

    See existing subclasses of ModelsBase for usage examples.

    """

    def __init__(self, database, model_names):
        self._base_model = None
        self._database = database
        self._database.connect()
        self._create_tables_if_necessary(model_names)

    def _create_tables_if_necessary(self, model_names):
        """Create tables for the models. Be silent if they already exist."""
        models = [getattr(self, name) for name in model_names]
        self._database.create_tables(models, True)

    @property
    def BaseModel(self):  # NOQA
        if self._base_model is None:
            class BaseModel(peewee.Model):
                class Meta:
                    database = self._database
            self._base_model = BaseModel
        return self._base_model
