# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import MatplotlibExamplesItem

class ExamplesSpider(scrapy.Spider):
    name = 'examples'
    allowed_domains = ['matplotlib.org']
    start_urls = ['https://matplotlib.org/examples/index.html']
    
    # 遍历所有例子的链接，并将链接形成request
    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//div[@class="toctree-wrapper compound"]',deny='/index.html$')
        links = le.extract_links(response)  # extract_links返回的是一个对象，不是URL，需要调用
        for link in links:
            yield scrapy.Request(link.url,callback=self.parse_example)
    
    # 解析例子页面，实现下载功能
    def parse_example(selef,response):
        href = response.xpath('//a[@class="reference external"]/@href').extract_first()
        url = response.urljoin(href)  # 这里要转为绝对路径
        example = MatplotlibExamplesItem()
        example['file_urls']=[url]   # 注意，这里是列表形式，要注意
        return example
        