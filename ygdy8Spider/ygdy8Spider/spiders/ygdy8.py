# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Ygdy8Spider(CrawlSpider):
    name = 'ygdy8'
    allowed_domains = ['ygdy8.net']
    start_urls = ['https://www.ygdy8.net/html/gndy/dyzz/index.html']
    # 解析网站资源，提取网址的方式、规则
    rules = (
        # 提取带有index.html的网址,这个就是导航栏的进入方式，其中游戏栏目不需要

        Rule(LinkExtractor(allow=r'index.html', deny='game|hytv|rihantv|oumeitv|zongyi2013|2009zongyi|dongman'), follow=False),
        # 提取每个栏目中下一页的链接,会提取重复的，但是scrapy会自动去重，格式是 list_8_2.html 格式，用正则表达式表示
        Rule(LinkExtractor(allow=r'list\d+_\d+.html', ),  follow=True),
        # 提取详情页数据,将响应交给函数处理
        Rule(LinkExtractor(allow=r'/\d+/\d+.html',), callback='parse_item', follow=True)
    )

    # 提取数据，清洗数据
    def parse_item(self, response):
        item = {}
        item = {
            'name': response.xpath('//h1/font/text()').get(),
            'ftp': response.xpath('//td[@style="WORD-WRAP: break-word"]/a/@href').get()
        }
        return item
