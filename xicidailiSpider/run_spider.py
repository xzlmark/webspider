# 运行爬虫文件，在pychram里面运行,要注意这个文件的位置，是位于scrapy,cfg一个目录下


# 第一中方式，必须加split()
from scrapy import cmdline
# cmdline.execute('scrapy crawl xicidaili'.split())

# 第二种是用os模块来实行
import os
os.system('scrapy crawl  xicidaili ')