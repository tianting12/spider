# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random
from time import strftime, localtime,sleep
import requests
import redis
from scrapy import signals


# from scrapy.utils.project import get_project_settings


class ZhihuSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class ZhihuDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    # user-agent随机请求头中间件

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.
        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

        # random.choice()在列表中随机选择一个
        # user_agent = random.choice(self.USER_AGENTS)
        # request.headers['User-Agent'] = user_agent
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

# 次数设置ip代理池和UA代理池
class UserAgentDownloadMiddleware(object):
    def __init__(self):
        self.pool = redis.ConnectionPool(host='127.0.0.1',
                                         port=6379,
                                         db=0,
                                         )
        self.conn = redis.StrictRedis(connection_pool=self.pool)
        # print(self.conn)
        # user-agent随机请求头中间件
    USER_AGENT = [
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
            'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0',
        ]
    # proxy = [
    #
    #     ]


    def process_request(self,request,spider):
        user_agent = random.choice(self.USER_AGENT)
        request.headers['User-Agent'] = user_agent

        # key = self.conn.srandmember('https')
        # print(key)
        proxy = self.conn.srandmember('https')
        proxy = proxy.decode('utf-8')
        ip = str(proxy)
        # print(ip)
        # ip = random.choice(self.proxy)
        request.meta['proxy'] = "https://%s" % ip


class IPProxyDownloadMiddleware(object):

    USER_AGENT = [
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
        'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6',
        'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.140 Safari/537.36 Edge/17.17134',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201',
        'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.57 Safari/537.17 SE 2.X MetaSr 1.0',
    ]

    def process_request(self, request, spider):
        while True:
            proxies = requests.get(url='http://127.0.0.1:5555/https').text
            if proxies == '43.255.228.150:3128':
                sleep(30)
                continue
            user_agent = random.choice(self.USER_AGENT)
            request.meta['proxy'] = 'https://' + proxies
            request.headers['User-Agent'] = user_agent
            break

    def process_response(self, request, response, spider):
        if response.status != 200:
            print(strftime("%Y-%m-%d %H:%M:%S", localtime()), f'\033[1;31;40m请求失败{response.url}\033[0m')
            proxies = requests.get(url='http://127.0.0.1:5555/https').text
            request.meta['proxy'] = 'https://' + proxies
            return request
        if response.status == 200:
            print(strftime("%Y-%m-%d %H:%M:%S", localtime()), f'\033[1;32;40m请求成功{response.url}\033[0m')
            return response

    def process_exception(self, request, exception, spider):
        print(strftime("%Y-%m-%d %H:%M:%S", localtime()), f'\033[1;31;40m重试{request.url}\033[0m')
        proxies = requests.get(url='http://127.0.0.1:5555/https').text
        request.meta['proxy'] = 'https://' + proxies
        return request


# class RandomProxyMiddleware(object):
#
#     def __init__(self):
#         settings = get_project_settings()
#         self.PROXY_REDIS_HOST = settings.get('PROXY_REDIS_HOST')
#         self.PROXY_REDIS_PORT = settings.get('PROXY_REDIS_PORT')
#         # self.PROXY_REDIS_PARAMS = settings.get('PROXY_REDIS_PARAMS')
#         self.PROXY_REDIS_KEY = settings.get('PROXY_REDIS_KEY')
#         self.pool = redis.ConnectionPool(host=self.PROXY_REDIS_HOST,
#                                          port=self.PROXY_REDIS_PORT,
#                                          db=0,)
#         self.conn = redis.StrictRedis(connection_pool=self.pool)
#
#     def process_request(self, request, spider):
#         proxy = self.conn.srandmember(self.PROXY_REDIS_KEY)
#         proxy = proxy.decode('utf-8')
#         ip = str(proxy)
#         request.meta['proxy'] = "https://%s" % ip
