# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MzituScrapyItem(scrapy.Item):
    name = scrapy.Field()   # 套图的名字
    image_urls = scrapy.Field()  # 图片地址
    url = scrapy.Field()
