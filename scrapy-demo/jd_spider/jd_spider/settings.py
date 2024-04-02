BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

# 日志级别
# LOG_LEVEL = 'INFO'

# Redis地址
REDIS_URL = 'redis://:Root.123456@test:6379/0'

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
    # 'jd_spider.middlewares.CookiesMiddleware': 543,
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
    'shshshfpa=841f5288-6c65-becb-dc02-8364792e3401-1672734445; shshshfp=dbe3f434230ba4f9807d90c69aecca75; shshshfpx=841f5288-6c65-becb-dc02-8364792e3401-1672734445; unpl=JF8EAK5nNSttC0oHBktWTxcYS1sDWw9fH0RUOzIFAFtcSQZWH1UeF0V7XlVdWBRKFR9sbhRUXFNLVw4bACsSEXteXVdZDEsWC2tXVgQFDQ8VXURJQlZAFDNVCV9dSRZRZjJWBFtdT1xWSAYYRRMfDlAKDlhCR1FpMjVkXlh7VAQrBhsQEE9bVltbOEonBF9XNVRZWUxUBisDKxMgCQkIV1QOTBILImMFVl1cTVYAHTIaIhM; __jdv=76161171|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_b0b2aee4917f4cfebfed1e753cb5f44d|1711591933405; __jdu=513157347; areaId=2; ipLoc-djd=2-2830-0-0; PCSYCityID=CN_310000_310100_0; _pst=jd_7a03396b3200d; unick=jd_166732wdn; pin=jd_7a03396b3200d; _tp=PpKqkUYY%2BbRRHsiPHJErUkoTT6uQ5ZrAHAKvEsJkd4A%3D; jsavif=1; mba_muid=513157347; mba_sid=17115937525285672487869092979.2; wlfstk_smdl=1izc2qc5t3x1ii2gyo1jpzxyv3xa4rh6; logintype=wx; npin=jd_7a03396b3200d; thor=78A0E8C7802AB08A7223341E687579666E02F09C64A627DC98BFCB586E215136EDA4963AF6DF9FD9376A23542EA3A543EBAF33E853482053D427846573E5E35D5536A6889B40FE30C6B4808A7432C5712FB519FC7AE2F13D323ECC865F5297C88AE83B8EC81ACCFF841B9E2D5CEB731FDC12ADA278EDAC168F15361BB3C6F00AA91A59EF32E8175F6DC5B3756E0B87A80A763710E095E3C41475657217FA0C10; flash=2_l2In2f9umMh9cGGypjKNgiAcXzXNN8HHduDlCYL-oT7kYaGGOmLMxEyRVgOIMW2IiAZFAVt2LB27BRe8gFbLosxEoaoCXlIwGq7PA8bheso*; pinId=yvjJW3zWHQ5lkdBSrJoHWLV9-x-f3wj7; avif=1; jsavif=1; xapieid=jdd03MZRFMA2DHJR3GUXYXROOPO6CZ254YILBD3FDQMINBCVJ635JDW5A7INDXDNH6RAOAG2R347RMMIXJYXQSWZEQZSCBQAAAAMOQLYXVCAAAAAADF5EFU4FPJVVREX; __jda=143920055.513157347.1711591932.1711591932.1711591933.1; __jdc=143920055; rkv=1.0; 3AB9D23F7A4B3CSS=jdd03MZRFMA2DHJR3GUXYXROOPO6CZ254YILBD3FDQMINBCVJ635JDW5A7INDXDNH6RAOAG2R347RMMIXJYXQSWZEQZSCBQAAAAMOQL6RVDQAAAAACR4SR5DGIQ7FBAX; __jdb=143920055.19.513157347|1.1711591933; qrsc=2; shshshfpb=BApXebYj1getA6fyYniJQf27L6hPC6IXbBzAyQ2pr9xJ1MqB6pYO2; 3AB9D23F7A4B3C9B=MZRFMA2DHJR3GUXYXROOPO6CZ254YILBD3FDQMINBCVJ635JDW5A7INDXDNH6RAOAG2R347RMMIXJYXQSWZEQZSCBQ'
]