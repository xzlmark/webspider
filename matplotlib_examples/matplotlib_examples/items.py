# -*- coding: utf-8 -*-

import scrapy


class MatplotlibExamplesItem(scrapy.Item):
    # 下面两个字段都是默认的属性， file_urls就是装的下载文件URL列表，files就是文件下载结果信息：
    # 信息包括：path：文件下载到本地的路径，下对路径
    # checksum: 文件的校验和
    # url :文件的url地址
    file_urls = scrapy.Field()
    files = scrapy.Field()
    
    
