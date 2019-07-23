# -*- coding: utf-8 -*-
import scrapy
import re

class BooksspiderSpider(scrapy.Spider):
    name = 'BooksSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        selectors = response.xpath('//article[@class="product_pod"]')
        for selector in selectors:
            name = selector.xpath('./h3/a/@title').get()
            price = selector.xpath('./div[@class="product_price"]/p[1]/text()').re('\d+.\d+')
            yield{
                'name':name,
                'price':price
            }
        next_page = response.xpath('//li[@class="next"]/a/@href').get()
        if next_page:
            next_url = response.urljoin(next_page)
           # print('-------------'+next_url)
            yield scrapy.Request(next_url,callback=self.parse)