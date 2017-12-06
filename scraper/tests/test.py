from unittest import TestCase
import datetime

from scraper.scraper import Scraper
from scraper.classes.options import AdvertOptions
from scraper.classes.autopscrapers import AutoPScraper
from scraper.classes.models import Advertisement

class ScraperTest(TestCase):

    def setUp(self):
        self.scraper = Scraper()

class AutoPScraperTest(TestCase): 

    def setUp(self):
        self.scraper = Scraper()
        self.scraper.set_autop(AdvertOptions.CARS)

    def test_car_scraper_selection(self): 
        '''
        Test if correct scraper selected by provided option
        '''
        self.assertEquals(AutoPScraper, type(self.scraper.type()))

    def test_particular_car_advert_scrape(self):
        '''
        Test paricular car advetisement scrape
        '''
        self.scraper.set_autop(AdvertOptions.CARS)
        # TODO FIX IT 
        url = 'file:///home/apoluden/Programming/workspace/reseller/scraper/tests/bmw_advertisement.html'
        scraped_advert = self.scraper.scrape_particular_advert(url)

class AdvertisementTest(TestCase):
    
    def test_created_at_field_assignement(self):
        '''
        Test created_at field UTC timestamp field assignement
        on Advertisement instance creation
        '''
        advert = Advertisement()
        self.assertEquals(datetime.datetime, type(advert.created_at))
        
