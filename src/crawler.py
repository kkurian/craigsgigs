import time

from .geosite import Geosite


class Crawler:
    def crawl(self):
        for geosite in Geosite.all():
            for locale in geosite.locales:
                for category in locale.categories:
                    for query in category.queries:
                        npp = query.next_page_parameters
                        while npp is not None:
                            time.sleep(1.0)
                            query.process_next_page_parameters(npp)
                            npp = query.next_page_parameters
