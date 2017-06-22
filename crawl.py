#!/usr/bin/env python

import logging

from src.crawler import Crawler


if '__main__' == __name__:
    logging.basicConfig(level=logging.DEBUG)
    Crawler().crawl()
