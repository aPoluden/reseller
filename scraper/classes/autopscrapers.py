from bs4 import BeautifulSoup
import urllib, requests
from requests.exceptions import ConnectionError, TooManyRedirects, Timeout, RequestException

from scraper.classes.options import AdvertOptions
from scraper.classes.models import Advertisement

class PortalScraper:

    def __init__(self, advert_type):
        self.advert_type = advert_type

    def scrape_particular_advert(self, url, path=None):
        pass

    def scrape_entire_adverts(self):
        pass

class AutoPScraper(PortalScraper):

    def __init__(self, advert_type):
        super(AutoPScraper, self).__init__(advert_type)
        if advert_type == AdvertOptions.CARS:
            self.scraper = AutoPCarScraper()
    
    def scrape_particular_advert(self, url, path=None):
        return self.scraper.get_particular_vehicle(url, path)

    def scrape_entire_adverts(self):
        return self.scraper.get_entire_vehicles()

    def type(self):
        '''
        returns: scraper instance
        '''
        return self.scraper

class VehicleScraper:
    
    def get_particular_vehicle(self, url, path=None):
        pass
    
    def get_entire_vehicles(self): 
        pass

class AutoPCarScraper(VehicleScraper):
    
    def __init__(self):
        super(AutoPCarScraper, self).__init__()

    def remove_spaces(self, raw): 
        return raw.replace(' ', '').replace('\n', '')

    def page_content(self, page_url, page_path=None):
        '''
        Returns WEB page HTML content
        params:
            page_url - web page resource url
            page_path - web page resource path
        returns:
            HTML content
        '''
        content = None
        try:
            if page_path:
                content = urllib.request.urlopen(page_path).read()
            else:
                content = requests.get(page_url).content
                resp = requests.get(page_url)
                if resp.status_code == 443 or resp.status_code == 429: 
                    # Dude Ur in blacklist
                    print('NOT WELCOME')
                    # TODO TOR
                    # TODO Logging
                content = resp.content
        except requests.exceptions.Timeout:
            print('Timeout')
        except requests.exceptions.TooManyRedirects:
            print('TooManyRedirects')
        except requests.exceptions.RequestException:
            print('RequestException')
        except requests.exceptions.ConnectionError:
            print('ConnectionError')
        except urllib.error.URLError:
            return None
        return content

    def get_car_advert_data(self, url, path=None):
        '''
        Scrapes AutoP store car advertisement
        returns: advertisement data
        '''
        advert, seller, vehicle = {}, {}, {}
        soup = BeautifulSoup(self.page_content(url, path), 'html.parser')
        element = soup.find_all(class_='add-to-bookmark')[0]
        advert_info = soup.find_all(class_='classifieds-info')[0]
        vehicle_specs = advert_info.find_all(class_='announcement-parameters')
        advert['uid'] = element.attrs['data-id']
        advert['name'] = advert_info.h1.text
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
        try:
            # Advert attributes that could be not defined
            advert['comment'] = advert_info.find(class_='announcement-description').text
        except AttributeError as e:
            # TODO Logging
            pass
        return {'vehicle': vehicle, 'advert': advert, 'seller': seller}
        
    def get_all_car_adverts_data(self):
        '''
        Scrapes all STORE car advertisements
        returns: all STORE car advertisements 
        '''
        soup = None
        current_page = 1
        url='https://autoplius.lt/skelbimai/naudoti-automobiliai'
        list_page = '/skelbimai/naudoti-automobiliai?page_nr={}'
        while True:
            list_url = url + list_page.format(current_page)
            content = self.page_content(list_url)
            soup = BeautifulSoup(content, 'html.parser')
            adverts_list = soup.find_all(class_='announcement-item')
            for advert in adverts_list:
                advert_url = advert['href']
                advert_data = self.get_car_advert_data(advert_url)
                yield advert_data
            current_page += 1
    
    def get_particular_vehicle(self, url, path=None):
        return self.get_car_advert_data(url, path)

    def get_entire_vehicles(self):
        return self.get_all_car_adverts_data()