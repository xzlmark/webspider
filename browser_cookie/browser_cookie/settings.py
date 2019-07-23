# -*- coding: utf-8 -*-

BOT_NAME = 'browser_cookie'

SPIDER_MODULES = ['browser_cookie.spiders']
NEWSPIDER_MODULE = 'browser_cookie.spiders'


ROBOTSTXT_OBEY = False


COOKIES_ENABLED = True  #如果有自定义中间件，必须为true


DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
   'User-Agent' :'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}


DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':None,
    'browser_cookie.middlewares.BrowserCookiesMiddleware': 1,
}