import scrapy
import ipdb

class DafitiSpider(scrapy.Spider):
    name = 'dafiti'
    start_urls = [
        'https://www.dafiti.com.br/catalog/?q=shoes&wtqs=1',
    ]
    
    def parse(self, response):
        products = response.xpath("//div[contains(@class,'main-list')]/*")
        for product in products:
            if product.css('.product-box-image a::attr(href)').get():
                data = {
                    'url': product.css('.product-box-image a::attr(href)').get(),
                    'img_url': product.css('.product-box-image a img::attr(data-original)').get(),
                    'brand': product.css('.product-box-brand::text').get(),
                    'title': product.css('.product-box-title::text').get(),
                    'from': product.css('.product-box-price-from::text').get(),
                    'to': product.css('.product-box-price-to::text').get(),
                }
                yield data