# -*- coding: utf-8 -*-
import scrapy


class DoubanItem(scrapy.Item):
    directors =scrapy.Field()
    rate = scrapy.Field()
    cover_x = scrapy.Field()
    star = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    casts = scrapy.Field()
    cover = scrapy.Field()
    movie_id = scrapy.Field()
    cover_y = scrapy.Field()