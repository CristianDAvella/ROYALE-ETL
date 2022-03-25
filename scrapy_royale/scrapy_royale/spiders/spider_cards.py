from unicodedata import name
import scrapy

# Estado actual: Extrae el nombre de todas las cartas en un archivo csv.
# Siquiente paso: guardar los nombres de las cartas sin espacios.
# Objetivo del dia: 


#   XPATH Sentenses
# Cards's lincks = //div[@class="card-overview"]//span[@class="mw-headline"]/a/@href
# Caeds's names = //div[@class="page-header__title-wrapper"]/h1/text()


class cards(scrapy.Spider):
    name = 'cards'
    start_urls = ['https://clashroyale.fandom.com/wiki/Card_Overviews']
    custom_settings = {
                        'FEED_URI':'cards.csv',
                        'FEED_FORMAT':'csv',
                        'FEED_EXPORT_ENCODING': 'utf-8'
                        }

    def parse(self, response):

        lincks = response.xpath('//div[@class="card-overview"]//span[@class="mw-headline"]/a/@href').getall()
        
        for linck in lincks:
            yield response.follow(linck, callback=self.get_info)
            
        

    def get_info(self, response):
        
        name = response.xpath('//div[@class="page-header__title-wrapper"]/h1/text()').get()

        yield {'names' : name}




