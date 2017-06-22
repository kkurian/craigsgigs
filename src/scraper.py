import re

from bs4 import BeautifulSoup
import peewee

from .database_factory import DatabaseFactory
from .models import Models


class Scraper:
    _db_class = peewee.SqliteDatabase
    _db_environment = 'production'
    _db = DatabaseFactory.build(_db_class, _db_environment)
    _models = Models(_db)

    def scrape(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        self._store_results(soup.find_all('p', class_='result-info'))
        return self._next_result_index(soup)

    def _store_results(self, tags):
        postings = list()
        for tag in tags:
            posted_at = tag.find('time')['datetime']
            text = tag.find('a').text
            url = tag.find('a')['href']
            postings.append({'posted_at': posted_at, 'text': text, 'url': url})
        if postings:
            self._models.Posting.insert_many(postings).execute()

    def _next_result_index(self, soup):
        totalcount = soup.find('span', class_='totalcount')
        if totalcount is not None:
            totalcount_int = int(totalcount.text)
            s_ = int(re.search(
                r's=(\d+)', soup.find('a', class_='next')['href']).group(1))
            if totalcount_int != s_:
                return s_
