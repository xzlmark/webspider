# -*- coding: utf-8 -*-
import scrapy


# 这个爬虫类必须是继承scrapy.Spider的类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']  # 开始采集的网址

# 解析响应的，下载器下载回来的数据以后交给这个函数来处理
    def parse(self, response):  # response就是下载器的返回
        # 提取IP和端口 response.selector返回的就是selector,内置的有xpath 和css方法；一般可以缩写成response.xpath() 或response.css()
        selectors = response.xpath('//table//tr')
        # 循环遍历tr标签
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()  # 提取数据
            port = selector.xpath('./td[3]/text()').get()
            if ip and port:
                yield {"ip": ip, "port": port}    # 如果需要将相关数据保存在数据库或文件中，这里一定要用yield，\
                # 并且是字典格式.同时要注意，这个会在日志中输出变量的值.
        # 翻页功能
        next_page = response.xpath("//a[@class='next_page']/@href").get()
        print('下一页是：----->'+next_page)
        if next_page:
            # next_url = 'https://www.xicidaili.com{0}'.format(next_page)
            next_url = response.urljoin(next_page)
            yield scrapy.Request(next_url, callback=self.parse)


