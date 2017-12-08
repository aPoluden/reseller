from bs4 import BeautifulSoup
import urllib

from scraper.classes.options import AdvertOptions
from scraper.classes.models import Advertisement

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

    def remove_spaces(self, raw): 
        return raw.replace(' ', '').replace('\n', '')

    def get_car_advert_data(self, url):
        '''
        Scrapes AutoP store car advertisement
        returns: advertisement data
        '''
        advert, seller, vehicle = {}, {}, {}
        resource = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(resource, 'html.parser')
        element = soup.find_all(class_='add-to-bookmark')[0]
        advert_info = soup.find_all(class_='classifieds-info')[0]
        vehicle_specs = advert_info.find_all(class_='announcement-parameters')
        advert['uid'] = element.attrs['data-id']
        advert['name'] = advert_info.h1.text
        advert['comment'] = advert_info.find(class_='announcement-description').text
        advert['location'] = self.remove_spaces(soup.find(class_='owner-location').text)
        seller['number'] = self.remove_spaces(soup.find(class_="announcement-owner-contacts").a.text)
        for param in vehicle_specs:
            # Vehicle specials
            param_rows = param.find_all('tr')
            for row in param_rows:
                spec_name = row.th.text
                spec_value = row.td.text
                if spec_name == 'Kaina Lietuvoje': 
                    advert['price'] = spec_value
                vehicle[spec_name] = spec_value
        return {'vehicle': vehicle, 'advert': advert, 'seller': seller}
        
    def get_all_car_adverts_data(self):
        '''extends arrow
        Scrapes all STORE car advertisements
        returns: all STORE car advertisements 
        '''
        yield None
    
    def get_particular_vehicle(self, url):
        return self.get_car_advert_data(url)