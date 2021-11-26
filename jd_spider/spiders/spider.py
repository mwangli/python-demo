import scrapy
import logging
from scrapy_redis.spiders import RedisSpider

from jd_spider.items import JDItem


class JobSpider(RedisSpider):
    name = 'spider'

    redis_key = 'spider:start_url'

    logger = logging.getLogger(None)

    # 列表页面解析
    def parse(self, response):
        # 获取商品节点列表
        node_list = response.xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
        temp = response.request.url.rpartition('=')
        self.logger.info(f'已获取第页{temp[2]}数据')
        self.logger.info(f'本页面共条{len(node_list)}数据')
        # 获取下一页
        next_url = temp[0] + temp[1] + str(int(temp[2]) + 1)
        yield scrapy.Request(next_url)
        # 遍历节点
        for node in node_list:
            # 获取商品sku
            item = JDItem()
            item['code'] = node.xpath('./@data-sku').extract_first()
            item['name'] = node.xpath('.//div[@class="p-img"]//a/@title').extract_first()
            item['price'] = node.xpath('.//div[@class="p-price"]//i/text()').extract_first()
            # 详情页面处理
            detail_url = 'https://item.jd.com/' + item['code'] + '.html'
            yield scrapy.Request(detail_url, callback=self.parse_detail, meta={'item': item})

    # 详情页面解析
    def parse_detail(self, response):
        # 获取item
        item = response.meta['item']
        item['category'] = response.xpath("//div[@id='crumb-wrap']//div[@class='item first']/a/text()")
        item['shop'] = response.xpath("//div[@class='crumb-wrap']//div[@class='name']/a/text()").extract_first()
        item['image'] = response.xpath('//*[@id="spec-img"]/@data-origin').extract_first()
        item['comments'] = response.xpath('//div[@id="comment-count"]/a/text()').extract_first()
        yield item
