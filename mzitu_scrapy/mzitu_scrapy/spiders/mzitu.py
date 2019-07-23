# -*- coding: utf-8 -*-
from scrapy import Request

import scrapy
from ..items import MzituScrapyItem


class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['mzitu.com']
    start_urls = ['http://mzitu.com/all',]
    img_urls = []  # 用来存储每个套图的全部图片的URL地址

    def parse(self, response):
        item = MzituScrapyItem()
        selectors = response.xpath('//ul[@class="archives"]/li/p/a')  # 图片包括标题和地址
        for selector in selectors:
            item['name'] = selector.xpath('./text()').get()
            item['url'] = selector.xpath('./@href').get()  # 把套图地址保存在列表中
            yield scrapy.Request(selector.xpath('./@href').get(), callback=self.parse_image)
            yield item

    def parse_image(self, response):  # //p/a/img/@src   https://www.mzitu.com/185752
        urls = response.xpath('//p/a/img/@src').get()
        yield {
            'image_urls': urls
        }

        # 下一页操作
        next_page = response.xpath('//div[@class="pagenavi"]/a[6]/@href').get()
        print('---------'+next_page)
        yield scrapy.Request(next_page, callback=self.parse_image)
