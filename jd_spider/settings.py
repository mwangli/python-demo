BOT_NAME = 'jd_spider'

SPIDER_MODULES = ['jd_spider.spiders']
NEWSPIDER_MODULE = 'jd_spider.spiders'

# 日志级别
LOG_LEVEL = 'INFO'

# Redis地址
REDIS_URL = 'redis://:Root.123456@47.99.44.141:6379'

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

# 并发请求数
CONCURRENT_REQUESTS = 4

# 下载延迟
DOWNLOAD_DELAY = 1

# IP代理列表
PROXY_LIST = [
    '61.164.39.68:53281',
    '115.218.7.133:9000',
]

# 用户代理列表
USER_AGENT_LIST = [
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
    'Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5',
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1',
    'Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10',
    'Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13',
    'Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+',
    'Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0',
    'Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)',
    'UCWEB7.0.2.37/28/999',
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
    'UCWEB7.0.2.37/28/999',
    'NOKIA5700/ UCWEB7.0.2.37/28/999',
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999'
]

# 爬取深度
# DEPTH_LIMIT = 100

# 登录cookies
COOKIES = 'shshshfpa=acfc8b11-3b55-e596-6dc1-e6daa521405b-1637896310;' \
          ' __jdv=122270672|direct|-|none|-|1637896310788; ' \
          'shshshfpb=d5BW%2FF2C2ArKmYvhh1BgoAw%3D%3D; ' \
          'areaId=15; ipLoc-djd=15-1213-3408-0; __jdu=16378963107881307024642; ' \
          'PCSYCityID=CN_330000_330100_330102; ' \
          'TrackID=1H8kmUGld_TLv9IQGkJw5QFUIwzSXtaJZPlaZvNlsaJnSRTTJvgsm9EKiHr3e0eOYave_DDF-NmR_RarVYJ4xfOjXTR4-kwJs1Yv4ib1Ttys; ' \
          'thor=78A0E8C7802AB08A7223341E687579666E02F09C64A627DC98BFCB586E215136F54F4C2881656A0AF23BE72DD9E8F935E32EB12504780A17444583CDEC9EE33596F41AAD6743C7331E29DFFC9F6C093BC9B0F7412BDC917F2EE1C0253610DB1EA5018BB9AB3A98DE1D898BF1CF0931E2DF8A9338C70D940793CB805D9CF9CD88D99883CEB711C0D1290AF394559325F0DE831EA76FD31C8EEF3D7A9769DEEBF3; ' \
          'pinId=yvjJW3zWHQ5lkdBSrJoHWLV9-x-f3wj7; pin=jd_7a03396b3200d; unick=jd_166732wdn; ceshi3.com=000; _tp=PpKqkUYY%2BbRRHsiPHJErUkoTT6uQ5ZrAHAKvEsJkd4A%3D;' \
          ' _pst=jd_7a03396b3200d; shshshfp=ec79367bbdaaf0e780cee333c3e9a1af; shshshsID=e7494c657eb42d7c74c1206923b23bd1_4_1637904997757; qrsc=1; __jda=122270672.16378963107881307024642.1637896311.1637896311.1637904899.2;' \
          ' __jdb=122270672.7.16378963107881307024642|2.1637904899; __jdc=122270672; rkv=1.0; 3AB9D23F7A4B3C9B=REOVK6FN33GL3CXEBAYVPB3A2ITBYWLU2QBCGN7WDG5PU2ZU7HZ4EXTIZALJN6B3Z35ZFWVPR2QN4ICOV5235YKMN4'
