BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

# 日志级别
# LOG_LEVEL = 'INFO'

# Redis地址
REDIS_URL = 'redis://:Root.123456@47.99.44.141:6379/1'

# 使用scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# 使用scrapy_redis的去重机制
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# 在ITEM_PIPELINES中添加redis管道
ITEM_PIPELINES = {
    # 'scrapy_redis.pipelines.RedisPipeline': 200
    'jd_spider.pipelines.MysqlPipeline': 300,
}

# 下载器中间件
DOWNLOADER_MIDDLEWARES = {
    'jd_spider.middlewares.UserAgentMiddleware': 543,
    'jd_spider.middlewares.CookiesMiddleware': 543,
    # 'jd_spider.middlewares.ProxyMiddleware': 543,
}

# 下载延迟
DOWNLOAD_DELAY = 1

# IP代理列表
PROXY_POOL = [
    '61.164.39.68:53281',
    '115.218.7.133:9000',
]

# 用户代理列表
USER_AGENT_POOL = [
    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0;',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11',
    'Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
]

# 爬取深度
DEPTH_LIMIT = 100

# 登录cookies
COOKIES_POOL = [
    'lang=zh-cn; UM_distinctid=17c2779000030e-056d0807a0896a-a7d173c-1fa400-17c27790001308; _yuque_session=SXe0oOFoJBOgxrYRPPJWVBJQYTusoK7Jx7dNwx7PnQBG4AwZpyyRpIHTca9SoiQHAqHpp_NPecy6Y1p34dHGrQ==; acw_tc=0bda732516379350883486388ef22ad8b18cc05dd3f55c81effadd482a607e; yuque_ctoken=-r0Df07xZD8SblCA61WN5mTm; CNZZDATA1272061571=1566519907-1599615260-%7C1637924944; _TRACERT_COOKIE__SESSION=4d3c930b-7fbc-4dbd-a622-b2600113b953; tree=a385%01c68828e1-5880-4d8b-95cd-c427d5b19df6%011'
]
