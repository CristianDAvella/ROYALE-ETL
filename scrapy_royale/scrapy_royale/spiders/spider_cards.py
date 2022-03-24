from unicodedata import name
import scrapy

# Estado actual: Este spider imprime los lincks relativos que lleva a las 106 cartas del juego.
# Siquiente paso: Usando el link relativo acceder al nombre de cada carta he imprimirlo.


#   XPATH Sentenses
# Cards's lincks = //div[@class="card-overview"]//span[@class="mw-headline"]/a/@href
# Caeds's names = //div[@class="page-header__title-wrapper"]/h1/text()


class cards(scrapy.Spider):
    name = 'cards'
    start_urls = ['https://clashroyale.fandom.com/wiki/Card_Overviews']

    def parse(self, response):
        cards = response.xpath('//div[@class="card-overview"]//span[@class="mw-headline"]/a/@href').getall()
        print('*'*100)
        for card in cards:
            print(f'- {card}')
        print('*'*100)
