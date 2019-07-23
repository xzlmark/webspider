# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest

class LonginspiderSpider(scrapy.Spider):
    name = 'loginSpider'
    allowed_domains = ['example.webscraping.com']
    # 爬取只能用户登录后才能爬取的数据
    start_urls = ['http://example.webscraping.com/places/default/user/profile']
    def parse(self, response):
        # 这里response是start_urls中返回的response
        if 'Welcome' in response.text:
            self.logger.info('登陆成功')
            yield {
                'name':response.xpath("//tr[@id='auth_user_first_name__row']/td[2]/text()").get()+
                        response.xpath("//tr[@id='auth_user_last_name__row']/td[2]/text()").get(),
                'email':response.xpath("//tr[@id='auth_user_email__row']/td[2]/text()").get()
            }

    # -----------------------------登录----------------------------
    login_url = 'http://example.webscraping.com/places/default/user/login'  # 需要登录的页面
    # 覆写父类方法，在开始时最先执行登录，而不是start_urls中的网址
    def start_requests(self):
        yield Request(self.login_url,callback=self.login)
    
    def login(self,response):
        # 登录页面的解析函数，构造FormRequest对象提交表单
        fd = {'email':'xzlmark@126.com','password':'123456'}
        yield FormRequest.from_response(response,formdata=fd,callback=self.parse_login)
    # 登录成功后，继续爬取start_urls中的页面。
    def parse_login(self,response):
    #注意：这里response是登陆后跳转的页面，http://example.webscraping.com/places/default/index#
    # 需要再次执行下面的请求，才会跳转到需要采集的页面中
        yield from super().start_requests()
        
        
        
        
