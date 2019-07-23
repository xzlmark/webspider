# -*- coding: utf-8 -*-
import scrapy


class ZhihuSpider(scrapy.Spider):
    name = 'baidu'
    # start_urls = ['https://baidu.com']

    def start_requests(self):
        yield scrapy.Request('http://i.baidu.com/',meta={'cookiejar':'chrome'})

    def parse(self, response):
        cookie = response.request.headers.getlist('Cookie')
        cookie1 = response.headers.getlist('Set-Cookie')
        print(cookie)
        print(cookie1)
        print(response.text)
