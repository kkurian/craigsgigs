import requests

from .scraper import Scraper


class Query:
    def __init__(self, search_term, category):
        self.search_term = search_term
        self.category = category
        self._result_index = 0
        self._scraper = Scraper()

    @property
    def s(self):
        return self._result_index

    @property
    def next_page_parameters(self):
        if self._result_index is None:
            result = None
        else:
            result = self._base_parameters
            # s is for pagination; it is the zero-based index to the first
            # result on the page; defaults to 0 when not provided
            if 0 < self._result_index:
                result.update({'s': self._result_index})
        return result

    def process_next_page_parameters(self, next_page_parameters):
        url = '{}/search/{}'.format(self.category.locale.url, self.category.id)
        r = requests.get(url, params=next_page_parameters)
        assert 200 == r.status_code
        self._result_index = self._scraper.scrape(r)

    @property
    def _base_parameters(self):
        result = {'query': self.search_term, 'is_telecommuting': 1}
        if 'cpg' == self.category:
            result.update({'is_paid': 'yes'})
        else:
            # part-time (2), contract (3), employee's choice (4)
            result.update({'employment_type': [2, 3, 4]})
        return result
