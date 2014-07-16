# Scraper for Massachusetts Appeals Court
# CourtID: massapp
#Court Short Name: MS
#Author: Andrei Chelaru
#Reviewer:
#Date: 2014-07-12

from juriscraper.opinions.united_states.state import mass
import re
import time
from datetime import date
from lxml import html, etree


class Site(mass.Site):
    def __init__(self):
        super(Site, self).__init__()
        self.court_id = self.__module__
        self.court_identifier = '(AC'
        self.grouping_regex = re.compile("(.*) \((AC \d+-P-\d+)\) \((.+)\)")