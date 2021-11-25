from jd_spider.settings import USER_AGENT_LIST
from jd_spider.settings import PROXY_LIST
from jd_spider.settings import COOKIES
import random


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(USER_AGENT_LIST)
        request.headers['User-Agent'] = user_agent


class CookiesMiddleware(object):
    def process_request(self, request, spider):
        cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in COOKIES.split(';')}
        request.cookies = cookies


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)
        request.meta['proxy'] = proxy['ip_port']
