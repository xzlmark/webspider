# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector

class Ygdy8SpiderPipeline(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def process_item(self, item, spider):
        sql = 'insert into ygdy(name,ftp) values (%s, %s)'  # 必须用这种方式，不然会报错；
        self.cursor.execute(sql, (item['name'], item['ftp']))  # 将上面的参数传进去
        self.db.commit()
        return item

    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.db = mysql.connector.connect(host='localhost', user='root', port=3306, passwd='123456', db='xzlmark',
                                          charset='gb2312')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()