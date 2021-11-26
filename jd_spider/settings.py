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
    'Openwave/ UCWEB7.0.2.37/28/999',
    'Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999',
]

# 爬取深度
# DEPTH_LIMIT = 100

# 登录cookies
COOKIES_POOL = [
    'pinId=yvjJW3zWHQ5lkdBSrJoHWLV9-x-f3wj7; __jdu=16284814869031387560296; shshshfpb=kLazNN8PfO2LxZGgLmSW8uQ==; shshshfpa=446db814-3d27-4c2a-5ded-ea738b6cfe8d-1611329249; unpl=V2_ZzNtbUIDRRwlCUNcexhdV2IKEwkSBUEVcgxAVntKDgxhVEBfclRCFnUURlVnG10UZwEZXkJcRxFFCEdkeR1ZAmYBEV1yZ3MWdThGVUsZWwZuBhtdR15EHXQKRlZyH1gCZgAaWnJnQx1yOHYfLkUyQyZBIl1CUEcQdwBEXXopXTVnAxNeRVJAF3MLdh8VGBEFYAAbWEtXRhxyAEdWextVA2MEE15KUHMURQs=; __jdv=76161171|direct|-|none|-|1637587688382; areaId=15; ipLoc-djd=15-1213-3411-0; PCSYCityID=CN_330000_330100_330106; pin=jd_7a03396b3200d; unick=jd_166732wdn; _tp=PpKqkUYY+bRRHsiPHJErUkoTT6uQ5ZrAHAKvEsJkd4A=; _pst=jd_7a03396b3200d; TrackID=1X6wBTu0ZK9c-RUVgEiANCvoZnsKO4vXpFGcws9V_beUcfR5HLzlUL6vvQumDyd7p5Z9MDU1nfFeVw4kOHSp-1_mbvRMyQkXs8D8b3gY6beg; user-key=24c43d9c-5c46-460e-89f6-de65a39c10c4; __jda=122270672.16284814869031387560296.1628481486.1637860509.1637922956.13; __jdc=122270672; shshshfp=086b68431df08a6966c3005bd944a8bc; token=0c1173d3089ccafceeac740ff20709ee,2,909957; __tk=usazuDv3Ysu1YDu5Xsk0vpdnuziRu3bRushFXUiSZsbRYzq0X3l3Xk,2,909957; shshshsID=a175170f992bc21308d70fb68b0279a6_7_1637923367766; __jdb=122270672.7.16284814869031387560296|13.1637922956; ip_cityCode=1213; 3AB9D23F7A4B3C9B=RCUOFJZQFP4XIMWZWP54XWUQ7OQDNUQNM635GFP5XBXNRGJX467I4QWAV4VP665FSWDJ2VYHQVPUEUFTJEHOE6FKS4'
]