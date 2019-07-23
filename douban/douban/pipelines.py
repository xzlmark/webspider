# -*- coding: utf-8 -*-

import mysql.connector
from .settings import MYSQL_DBNAME,MYSQL_HOST,MYSQL_PASSWORD,MYSQL_USER
from twisted.enterprise import adbapi
import pymysql


# 这个不是异步操作，在没执行一条数据就调用一次commit，数据库可能瘫痪
class MysqlPipeline(object):
    def __init__(self):
        host =MYSQL_HOST
        port = 3306
        user = MYSQL_USER
        password = MYSQL_PASSWORD
        dbname = MYSQL_DBNAME
        self.db = mysql.connector.connect(host=host,port=port,user=user,password=password,db=dbname,charset='utf8')
        self.cursor = self.db.cursor()

    def process_item(self, item, spider):
        sql = 'insert into douban_movie(directors,rate,cover_x,star,title,url,casts,cover,movie_id,cover_y) values ' \
              '(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)'   # 必须用这种方式，不然会报错；
        self.cursor.execute(sql, (item['directors'], item['rate'], item['cover_x'], item['star'], item['title'], item['url'],
                                  item['casts'], item['cover'], item['movie_id'], item['cover_y']))   # 将上面的参数传进去
        return item

    def close_spider(self, spider):
        self.db.commit()    # 数据量大的时候有可能造成数据丢失，可以放在process_item中，但是插入一条数据就提交一次
        self.cursor.close()
        self.db.close()


# 这个是异步，但是有问题，不知道是什么原因，插入了重复数据
class MysqlPipeline_sys(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):
        dbparms = dict(
            host=settings["MYSQL_HOST"], db=settings["MYSQL_DBNAME"], user=settings["MYSQL_USER"],
            passwd=settings["MYSQL_PASSWORD"], charset='utf8', cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,)
        dbpool = adbapi.ConnectionPool("pymysql", **dbparms)
        return cls(dbpool)

    def process_item(self, item, spider):
        self.dbpool.runInteraction(self.insert_db, item)
        return item

    def insert_db(self, tx, item):
        sql = 'insert into douban_movie(directors,rate,cover_x,star,title,url,casts,cover,movie_id,cover_y) values ' \
              '(%s, %s,%s, %s,%s, %s,%s, %s,%s, %s)'   # 必须用这种方式，不然会报错；
        values = (
            item['directors'], item['rate'], item['cover_x'], item['star'], item['title'], item['url'],
            item['casts'], item['cover'], item['movie_id'], item['cover_y']
        )
        tx.execute(sql, values)   # 将上面的参数传进去

    def close_spider(self, spider):
        self.dbpool.close()
