# -*- coding: utf-8 -*-
import json
import scrapy

class ImagesSpider(scrapy.Spider):
    
    BASE_URL = 'http://image.so.com/zjl?ch=beauty&sn=%s&listtype=new&temp=1'
    start_index = 0
    # 限制最大下载数量，防止磁盘用量过大
    MAX_DOWNLOAD_NUM= 100
    name = 'images'
    #allowed_domains = ['image.so.com']
    start_urls = [BASE_URL % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf8'))
        # 提取所有图片下载URL到一个列表，赋给item的'image_urls'
        # json文件中有一个list列表，列表中才有图片URL;下面这种是列表推导式
        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}
        # 如果count字段大于0，并且下载数量不足100时下载图片
        self.start_index += infos['count']
        if infos['count'] > 0 and self.start_index<self.MAX_DOWNLOAD_NUM:
            yield scrapy.Request(self.BASE_URL % (self.start_index),callback=self.parse)
