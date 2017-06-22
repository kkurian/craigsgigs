from .query import Query


class Category:
    SEARCH_TERMS = ['python | ruby', 'backend']

    def __init__(self, id_, locale):
        self.id = id_
        self.locale = locale

    @property
    def queries(self):
        for search_term in self.SEARCH_TERMS:
            yield Query(search_term, self)
