import scrapy
from jd_spider.items import JDItem


class JobSpider(scrapy.Spider):
    name = 'spider'
    allowed_domains = ['jd.com']
    start_urls = [
        'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&wq=%E6%89%8B%E6%9C%BA&pvid=cbb8de4071f84668b92a8258d4b4ec04&page=1'
    ]

    # 列表页面解析
    def parse(self, response):
        # 获取商品节点列表
        node_list = response.xpath("//div[@id='J_goodsList']//li[@class='gl-item']")
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
            # 获取下一页
            temp = response.request.url.rpartition('=')
            next_url = temp[0] + temp[1] + str(int(temp[2]) + 1)
            yield scrapy.Request(next_url)

    # 详情页面解析
    def parse_detail(self, response):
        # 获取item
        item = response.meta['item']
        item['category'] = response.xpath("//div[@id='crumb-wrap']//div[@class='item first']/a/text()").extract_first()
        item['shop'] = response.xpath("//div[@class='crumb-wrap']//div[@class='name']/a/text()").extract_first()
        item['image'] = response.xpath('//*[@id="spec-img"]/@data-origin').extract_first()
        item['comments'] = response.xpath('//div[@id="comment-count"]/a/text()').extract_first()
        # print(item)
        yield item
