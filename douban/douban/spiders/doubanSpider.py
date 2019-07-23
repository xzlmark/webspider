# -*- coding: utf-8 -*-
import json
import scrapy
from ..items import DoubanItem

class DoubanspiderSpider(scrapy.Spider):
    name = 'doubanSpider'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start=0']

    def parse(self, response):
        url = 'https://movie.douban.com/j/new_search_subjects?sort=U&range=0,10&tags=&start={0}'
        item = DoubanItem()
        infos = json.loads(response.text)
        for info in infos['data']:
            item['directors'] = str(info['directors'])
            item['rate'] = info['rate']
            item['cover_x'] = info['cover_x']
            item['star'] = info['star']
            item['title'] = info['title']
            item['url'] = info['url']
            item['casts'] = str(info['casts'])
            item['cover'] = info['cover']
            item['movie_id'] = info['id']
            item['cover_y'] = info['cover_y']
            yield item
            # for i in range(20, 9980, 20):
        for i in range(20, 9980, 20):   # 返回9971条数据
            yield scrapy.Request(url.format(i))

