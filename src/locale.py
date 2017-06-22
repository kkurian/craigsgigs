from bs4 import BeautifulSoup
import requests

from .categories import CATEGORIES
from .category import Category


class Locale:
    def __init__(self, tag):
        self.url = tag.get('href')
        self.name = tag.text

    @property
    def categories(self):
        r = requests.get(self.url)
        assert 200 == r.status_code
        soup = BeautifulSoup(r.text, 'html.parser')
        for category in CATEGORIES:
            if soup.find('a', class_=category):
                yield Category(category, self)
