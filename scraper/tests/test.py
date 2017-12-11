from unittest import TestCase
import datetime

from scraper.scraper import Scraper
from scraper.classes.options import AdvertOptions
from scraper.classes.autopscrapers import AutoPScraper, AutoPCarScraper
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
        # TODO FIX IT USE PYTHONPATH
        url = 'file:///home/apoluden/Programming/workspace/reseller/scraper/tests/bmw_advertisement.html'
        scraped_advert = self.scraper.scrape_particular_advert(None, path=url)
        vehicle = scraped_advert['vehicle']
        advert = scraped_advert['advert']
        seller = scraped_advert['seller']
        self.assertEquals('+37069157207', seller['number'])
        self.assertEquals('5004458', advert['uid'])
        self.assertEquals('Panevėžys,Lietuva', advert['location'])
        self.assertEquals('10 900 €', advert['price'])
        self.assertEquals('BMW 520, 2.0 l., universalas', advert['name'])

    def test_entire_car_advert_scrape(self): 
        '''
        Tests all available car advert scraping
        '''
        generator = self.scraper.scrape_entire_adverts()
        while True:
            print(next(generator))

    def test_bad_webpage_url_or_path(self):
        '''
        Tests wrong URL or path
        '''
        wrong_path = 'file://wrong/path'
        wrong_url = 'http://wrong.url'
        scraper = AutoPCarScraper()
        self.assertIsNone(scraper.page_content(wrong_url))
        self.assertIsNone(scraper.page_content(None, wrong_path))

    def test_entire_car_scrape_url_unreachable(self):
        '''
        Test entrire adverts scrape when URL unreachable/not exists/ip blocked
        '''
        # TODO
        pass

class AdvertisementTest(TestCase):
    
    def test_created_at_field_assignement(self):
        '''
        Test created_at field UTC timestamp field assignement
        on Advertisement instance creation
        '''
        advert = Advertisement()
        self.assertEquals(datetime.datetime, type(advert.created_at))
        
