# -*- coding: utf-8 -*-

import mysql.connector
import pymongo
from .settings import mysql_host,mysql_port,mysql_db,mysql_password,mysql_user
from .settings import mongo_host,mongo_port,mongo_db_name,mongo_db_collection
# class MysqlPipeline(object):
#     def __init__(self):
#         host =mysql_host
#         port = mysql_port
#         user = mysql_user
#         password = mysql_password
#         dbname = mysql_db
#         self.db = mysql.connector.connect(host=host,port=port,user=user,password=password,db=dbname,charset='utf8')
#         self.cursor = self.db.cursor()
#
#     def process_item(self, item, spider):
#         sql = 'insert into xicidaili(ip,port) values (%s, %s)'   # 必须用这种方式，不然会报错；
#         self.cursor.execute(sql, (item['ip'], item['port']))   # 将上面的参数传进去
#         self.db.commit()
#         return item
#
#     # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次,这个方法也可以。
#     # def open_spider(self, spider):
#     #     self.db = mysql.connector.connect(host='localhost', user='root', port=3306, passwd='123456', db='xzlmark', charset='utf8')
#     #     self.cursor = self.db.cursor()
#
#     def close_spider(self, spider):
#         print('---------------------close')
#         self.cursor.close()
#         self.db.close()

class MyMongoPipeline(object):
    def __init__(self):
        host =mongo_host
        port = mongo_port
        dbname = mongo_db_name
        sheetname = mongo_db_collection
        # 建立数据库连接
        self.conn = pymongo.MongoClient(host=host, port=port)
        # 通过连接找到数据库
        mydb= self.conn[dbname]
        # 通过数据库找到集合
        self.post = mydb[sheetname]

    def process_item(self, item, spider):
        # 必须将数据转为字典格式
       data = dict(item)
        # 调用insert方法插入
       self.post.insert(data)
       return item


    def close_spider(self, spider):
        self.conn.close()