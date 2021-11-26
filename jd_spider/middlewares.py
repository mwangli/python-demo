from jd_spider.settings import USER_AGENT_POOL
from jd_spider.settings import PROXY_POOL
from jd_spider.settings import COOKIES_POOL
import random


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_POOL)
        request.headers['User-Agent'] = user_agent


class CookiesMiddleware(object):
    def process_request(self, request, spider):
        cookies_str = random.choice(COOKIES_POOL)
        cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies_str.split(';')}
        request.cookies = cookies


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXY_POOL)
        request.meta['proxy'] = proxy
