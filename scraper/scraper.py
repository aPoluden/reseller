from scraper.classes.autopscrapers import AutoPScraper

class Scraper:
    '''
    Entrypoint
    '''
    def __init__(self):
        pass

    def set_autop(self, advert_type):
        '''
        Sets PortalScraper type
        params:
            advert_type type of advertisement
        '''
        self.scraper = AutoPScraper(advert_type)

    def scrape_particular_advert(self, advert_url):
        '''
        Scrapes Portal particular adverisement URL
        returns: scraped advertisement data
        '''
        return self.scraper.scrape_particular_advert(advert_url)
 
    def scrape_entire_adverts(self):
        pass

    def type(self):
        '''
        returns: Scraper instance
        '''
        return self.scraper