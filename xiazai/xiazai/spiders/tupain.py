import scrapy


class TupainSpider(scrapy.Spider):
    name = 'tupain'
    allowed_domains = ['w.wallhaven.cc']
    start_urls = ['http://w.wallhaven.cc/']

    def parse(self, response):
        pass
