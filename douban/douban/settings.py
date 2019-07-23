# -*- coding: utf-8 -*-

# Scrapy settings for douban project

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'


# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 0.25


# Disable cookies (enabled by default)
#COOKIES_ENABLED = False



DOWNLOADER_MIDDLEWARES = {
'douban.middlewares.MyUserAgent':542,
# 'douban.middlewares.MyProxy': 543,
}


ITEM_PIPELINES = {
   'douban.pipelines.MysqlPipeline': 300,
}
# MySQL 数据库配置
MYSQL_HOST = "localhost"
MYSQL_DBNAME = "xzlmark"
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"

