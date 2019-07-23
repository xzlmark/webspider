from scrapy import cmdline

cmdline.execute('scrapy crawl bookSpider -o data.jl'.split())