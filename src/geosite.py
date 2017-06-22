from bs4 import BeautifulSoup
import requests

from .locale import Locale


class Geosite:
    def __init__(self, tag):
        self.url = f'https:{tag.get("href")}'
        self.state = tag.text

    @staticmethod
    def all():
        r = requests.get('https://boulder.craigslist.org/')
        assert 200 == r.status_code
        soup = BeautifulSoup(r.text, 'html.parser')
        tags = soup.find('h5', text='us states').next_sibling.find_all('a')
        for tag in tags:
            yield Geosite(tag)

    @property
    def locales(self):
        for tag in self._geositelist.find_all('a'):
            yield Locale(tag)

    @property
    def _geositelist(self):
        r = requests.get(self.url)
        assert 200 == r.status_code
        soup = BeautifulSoup(r.text, 'html.parser')
        geositelist = soup.find_all('ul', class_='geo-site-list')
        assert 1 == len(geositelist)
        return geositelist[0]

