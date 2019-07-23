# -*- coding: utf-8 -*-

# Scrapy settings for mzitu_scrapy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'mzitu_scrapy'

SPIDER_MODULES = ['mzitu_scrapy.spiders']
NEWSPIDER_MODULE = 'mzitu_scrapy.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mzitu_scrapy (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}


SPIDER_MIDDLEWARES = {
    'mzitu_scrapy.middlewares.MzituDownloaderMiddlewareUseragent': 543,
}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
'mzitu_scrapy.middlewares.MzituFerer': 543,
'mzitu_scrapy.middlewares.MzituDownloaderMiddlewareUseragent':542,
# 'mzitu_scrapy.middlewares.IPProxyMiddleware':541

}

ITEM_PIPELINES = {
'scrapy.pipelines.images.ImagesPipeline': 1,
'mzitu_scrapy.pipelines.MzituScrapyPipeline': 300,
}
IMAGES_STORE = r'E:\python\project\mzitu_scrapy'    # 图片保存路径
# IMAGES_EXPIRES = 30   # 图像管道避免下载最近已经下载的图片。使用 FILES_EXPIRES (或 IMAGES_EXPIRES) 设置可以调整失效期限，可以用天数来指定:
