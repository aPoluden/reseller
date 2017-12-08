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
        Tests paricular car advetisement scrape
        '''
        self.scraper.set_autop(AdvertOptions.CARS)
        # TODO FIX IT 
        url = 'file:///home/apoluden/Programming/workspace/reseller/scraper/tests/bmw_advertisement.html'
        scraped_advert = self.scraper.scrape_particular_advert(url)
        vehicle = scraped_advert['vehicle']
        advert = scraped_advert['advert']
        seller = scraped_advert['seller']
        self.assertEquals('+37069157207', seller['number'])
        self.assertEquals('5004458', advert['uid'])
        self.assertEquals('Panevėžys,Lietuva', advert['location'])
        self.assertEquals('10 900 €', advert['price'])
        self.assertEquals('BMW 520, 2.0 l., universalas', advert['name'])

class AdvertisementTest(TestCase):
    
    def test_created_at_field_assignement(self):
        '''
        Test created_at field UTC timestamp field assignement
        on Advertisement instance creation
        '''
        advert = Advertisement()
        self.assertEquals(datetime.datetime, type(advert.created_at))
        
