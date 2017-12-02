from scraper.classes.options import AdvertOptions

class PortalScraper:

    def __init__(self, advert_type):
        self.advert_type = advert_type

    def scrape_particular_advert(self, url):
        pass

    def scrape_entire_adverts(self):
        pass

class AutoPScraper(PortalScraper):

    def __init__(self, advert_type):
        super(AutoPScraper, self).__init__(advert_type)
        if advert_type == AdvertOptions.CARS:
            self.scraper = AutoPCarScraper()
    
    def scrape_particular_advert(self, url):
        return self.scraper.get_particular_vehicle(url)

    def scrape_entire_adverts(self):         
        pass

    def type(self):
        '''
        returns: scraper instance
        '''
        return self.scraper

class VehicleScraper:
    
    def get_particular_vehicle(self, url):
        pass
    
    def get_entire_vehicles(self): 
        pass

class AutoPCarScraper(VehicleScraper):
    
    def __init__(self):
        super(AutoPCarScraper, self).__init__()

    def get_car_advert_data(self, url):
        '''
        Scrapes particular STORE car advertisementnoi
        returns: STORE car advertisement data
        '''
        return 'test'

    def get_all_car_adverts_data(self):
        '''extends arrow
        Scrapes all STORE car advertisements
        returns: all STORE car advertisements 
        '''
        yield None
    
    def get_particular_vehicle(self, url):
        return self.get_car_advert_data(url)