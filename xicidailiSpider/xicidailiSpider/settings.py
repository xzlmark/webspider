# -*- coding: utf-8 -*-

BOT_NAME = 'xicidailiSpider'

SPIDER_MODULES = ['xicidailiSpider.spiders']
NEWSPIDER_MODULE = 'xicidailiSpider.spiders'

CLOSESPIDER_ITEMCOUNT =300 # 爬虫爬取300条数据自动退出

# Obey robots.txt rules   是否遵守机器人协议，选择否
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32


# See also autothrottle settings and docs  配置下载延迟时间，时间为秒
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default) 是否启用cookie
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False


# Enable or disable downloader middlewares  配置下载中间件，request和response都可以设置

DOWNLOADER_MIDDLEWARES = {
'xicidailiSpider.middlewares.MyUserAgent':543,
# 'xicidailiSpider.middlewares.MyProxy':544,
}


# Configure item pipelines   数据保存

ITEM_PIPELINES = {
# 'xicidailiSpider.pipelines.MysqlPipeline': 300,
'xicidailiSpider.pipelines.MyMongoPipeline':301
}

# MySQL 数据库配置
mysql_host = '127.0.0.1'
mysql_port = '3306'
mysql_user = 'root'
mysql_password = '123456'
mysql_db = 'xzlmark'

# MongoDB数据库配置
mongo_host = '127.0.0.1'
mongo_port = 27017
mongo_db_name ='xzlmark'
mongo_db_collection = 'xicidaili'
