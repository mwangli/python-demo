import scrapy
from scrapy import Spider

from scrapy_redis.spiders import RedisSpider

from jd_spider.items import JDItem


# class JobSpider(RedisSpider):
class JobSpider(Spider):
    name = 'jd_spider'

    # redis_key = 'spider:start_url'
    start_urls = [
        'https://search.jd.com/Search?keyword=%E6%B1%89%E6%9C%8D&page=1']

    # 列表页面解析
    def parse(self, response):
        # 获取商品节点列表
        node_list = response.xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
        # print(node_list)
        # 遍历节点
        for node in node_list:
            # 获取商品sku
            item = JDItem()
            item['code'] = node.xpath('./@data-sku').extract_first()
            item['name'] = node.xpath('.//div[@class="p-img"]//a/@title').extract_first()
            item['price'] = node.xpath('.//div[@class="p-price"]//i/text()').extract_first()
            # yield item
            # 详情页面处理
            detail_url = 'https://item.jd.com/' + item['code'] + '.html'
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})
        # 获取下一页,页面深度+1即可
        temp = response.request.url.rpartition('=')
        next_url = temp[0] + temp[1] + str(int(temp[2]) + 2)
        print("下一页URL:", next_url)
        yield scrapy.Request(next_url)

    # 详情页面解析
    def parse_detail(self, response):
        # 获取item
        item = response.meta['item']
        item['category'] = response.xpath("//div[@id='crumb-wrap']//div[@class='item first']/a/text()").extract_first()
        item['shop'] = response.xpath("//div[@class='crumb-wrap']//div[@class='name']/a/text()").extract_first()
        item['image'] = response.xpath('//*[@id="spec-img"]/@data-origin').extract_first()
        item['comments'] = response.xpath('//div[@id="comment-count"]/a/text()').extract_first()
        yield item
