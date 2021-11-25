import scrapy


class SpiderSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['jd.com']
    start_urls = ['http://jd.com/']

    def parse(self, response):
        pass
