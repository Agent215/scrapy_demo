import scrapy
from bs4 import BeautifulSoup as soup

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ['bestbuy.com']
    start_urls = [
        'https://www.bestbuy.com/site/searchpage.jsp?st=graphics+cards&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=1&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys',
        'https://www.bestbuy.com/site/searchpage.jsp?st=graphics+cards&_dyncharset=UTF-8&_dynSessConf=&id=pcat17071&type=page&sc=Global&cp=2&nrp=&sp=&qp=&list=n&af=true&iht=y&usc=All+Categories&ks=960&keys=keys',
    ]     
        


    def parse(self, response):
        print("respone" +str(response))
        # page = response.url.split("/")[-2]
        result = response.url.find('cp')
        page = response.url[130 : 131]
        print("page number " + str(page))
        print("result of cp " + str(result))
        filename = f'graphics-cards-{page}.html'
        page_soup = soup(response.body, "html.parser")
        cards = page_soup.findAll("li", {"class": "sku-item"})
        print("number of cards "+str(len(cards)))
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')