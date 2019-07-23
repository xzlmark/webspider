# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from ..items import ToscrapeItem
class BookspiderSpider(scrapy.Spider):
    name = 'bookSpider'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    # 书籍列表页面解析函数，完成两件事情：
    # 1、提取页面中每一个书籍页面的链接，用他们构造request对象并提交
    # 2、提取页面中下一个书籍列表页面的链接，用其构造request对象并提交
    def parse(self, response):
        le = LinkExtractor(restrict_xpaths='//article[@class="product_pod"]')
        for link in le.extract_links(response):
            yield scrapy.Request(link.url,callback=self.parse_book)
            # 使用LInkExtractor提取下一页的按钮
        le = LinkExtractor(restrict_xpaths='//li[@class="next"]')
        links = le.extract_links(response)
        if links:
            next_url = links[0].url
            yield scrapy.Request(next_url,callback=self.parse)
    
    # 书籍页面解析函数  ('star-rating ([A-Za-z]+)')
    def parse_book(self,response):
        book = ToscrapeItem()
        selectors = response.xpath('//div[@class="col-sm-6 product_main"]')
        for selector in selectors:
            book['name'] = selector.xpath('./h1/text()').extract_first()
            book['price'] = selector.xpath('./p[@class="price_color"]/text()').re('\d+.\d+')
            book['review_rating'] = selector.xpath('./p[3]/@class').re_first('star-rating ([A-Za-z]+)')  # star-rating Three
            
        selectors = response.xpath('//table[@class="table table-striped"]')
        book['upc'] =selectors.xpath('.//tr[1]/td/text()').extract_first()
        book['stock'] = selectors.xpath('.//tr[last()-1]/td/text()').re('\d+')
        book['review_num'] = selectors.xpath('.//tr[last()]/td/text()').extract_first()
        yield book
