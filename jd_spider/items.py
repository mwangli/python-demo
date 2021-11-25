import scrapy


class JDItem(scrapy.Item):
    code = scrapy.Field()
    category = scrapy.Field()
    shop = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    image = scrapy.Field()
    comments = scrapy.Field()
