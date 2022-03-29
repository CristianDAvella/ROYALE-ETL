from unicodedata import name
import scrapy

# Estado actual: Extrae informacion de todas las cartas en un archivo csv.
# Siquiente paso: tipear informacion usando pandas.
# Objetivo del dia: 


#   XPATH Sentenses
# Cards's lincks = //div[@class="card-overview"]//span[@class="mw-headline"]/a/@href
# Cards's names = //div[@class="mw-parser-output"]//h2[@class="pi-item pi-item-spacing pi-title pi-secondary-background"]/text()
# Cards's description = //div[@class="quote-block"]/i/b/text()
# Cards's cost = //div[@data-source="Cost"]/div[@class="pi-data-value pi-font"]/text()
# Cards's rarity = //div[@data-source="Rarity"]/div[@class="pi-data-value pi-font"]/text()




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
        
        name = response.xpath('//div[@class="mw-parser-output"]//h2[@class="pi-item pi-item-spacing pi-title pi-secondary-background"]/text()').get()
        description = response.xpath('//div[@class="quote-block"]/i/b/text()').get()
        cost = response.xpath('//div[@data-source="Cost"]/div[@class="pi-data-value pi-font"]/text()').get()
        rarity = response.xpath('//div[@data-source="Rarity"]/div[@class="pi-data-value pi-font"]/text()').get()

        info = {'names' : name,
                'description' : description,
                'cost' : cost,
                'rarity' : rarity}

        return info




