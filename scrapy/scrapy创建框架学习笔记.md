# 一、scrapy开发项目的步骤

## （一）创建项目

​	在开始爬虫前，先要创建项目。进入你需要放置项目的文件夹，然后启动CMD命令行，切换到该目录下，在命令行中输入：scrapy start 项目名（一般为网站域名）。例如：scrapy startproject maoyan。

​	创建后的目录结构为：

​	![](.\image\模版目录结构.png)

​	相应目录的作用如下：

![1560568979634](.\image\目录结构作用.png)

​	       

## （二）创建爬虫文件

​	第一步创建项目后，只有scrapy的模版文件，但是我们需要创建爬虫文件，在爬虫文件写我们的主要代码，这个文件也是我们主要完成的。cd进入刚才创建的项目目录，这个目录就是项目的根目录，然后在命令行中输入：scrapy genspider  爬虫Spider  域名.com。如：scrapy genspider maoyanSpider maoyan。这样，就多了一个spider文件。爬虫文件编写如下：官方的方式：<scrapy genspider mydomain mydomain.com>

```python
import scrapy

# 这个爬虫类必须是继承scrapy.Spider的类
class XicidailiSpider(scrapy.Spider):
    name = 'xicidaili'
    allowed_domains = ['xicidaili.com']
    start_urls = ['https://www.xicidaili.com/nn/']  # 开始采集的网址,如果没有使用start_requests()方法，则这个是必须要有的

# 解析响应的，下载器下载回来的数据以后交给这个函数来处理
    def parse(self, response):  # response就是下载器的返回
        # 提取IP和端口，selector是scrapy提供的选择器，当然这里也可以用beautifusoup代替,一般用xpath和css，re()方法必须在xpath和css方法后才能调用。
        selectors = response.xpath('//table//tr')   # 这个里面就包含了所需要提取的内容，官方推荐使用xpath进行选择，css也可以选择，但是css实际上也是调用xpath实现的
        # 循环遍历tr标签
        for selector in selectors:
            ip = selector.xpath('./td[2]/text()').get()  # 提取数据，这里必须要用get() 方法，不然就是一个selector对象。有get()和getall()方法，如果不用这两种，还可以使用re()方法。如：response.css('title::text').re(r'Q\w+')
            port = selector.xpath('./td[3]/text()').get()  # 还有getall() 方法、extract_first()、extract()方法。getall()=extract(),get()=extract_first()
            if ip and port:						# and和or是短路运算符，and是求假，or是求真
                yield {"ip": ip, "port": port}    # 如果需要将相关数据保存在数据库或文件中，这里一定要用yield，并且是字典格式。这里会在日志中输出参会参数。也可以将Item类导入，然后给Item传值：yield Item（ip=ip）
        # 翻页功能
        next_page = response.xpath("//a[@class='next_page']/@href").get()  # 下一页的超链接
        print('下一页是：----->'+next_page)
        if next_page:
            next_url = 'https://www.xicidaili.com{0}'.format(next_page)   # 匹配下一页的完整URL
            yield scrapy.Request(next_url, callback=self.parse)    # 用yield方法重新调用Requests方法，这个方法中有URL参数，callback，meta等参数
            # 这里也可以使用yield response.follow(next_page, callback=self.parse),这里next_page可以使用相对地址，支持传递selector参数，具体区别见下面
```

如果需要使用start_requests()方法，则如下：

```python
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
```

# （三）启动爬虫

​	第一种方式：在项目的根目录下，在命令行中输入：scrapy crawl 项目名。

​	第二种方式：在根目录下，创建运行文件：run_spider.py

```python
import os
os.system('scrapy crawl xicidaili')


```

# （四）保存爬取到的数据

​	scrapy在parse回调函数中，用yield返回需要保存的数据

​	最简单的方式保存数据是用命令：scrapy crawl 项目名 -o file.json   --->就是将数据保存为json数据，注意：json数据文件只能运行一次，运行两次json数据文件是一个破损文件，这是历史原因导致的。

​	其次可以用: scrapy crawl -o file.jl 将数据保存为json Lines文件，避免了json的上述问题，同时数据是按行保存的。

​	还可以导出XML、CSV格式的文件，格式如上。

​	再次可以在pipelines.py中编写数据存储管道，同时要注意在settings中设置。管道文件：

```python
import mysql.connector

class XicidailispiderPipeline(object):
    def __init__(self):
        self.db = None
        self.cursor = None

    def process_item(self, item, spider):   # 必须要有这个方法
        sql = 'insert into xicidaili(ip,port) values (%s, %s)'   # 必须用这种方式，不然会报错；
        self.cursor.execute(sql, (item['ip'], item['port']))   # 将上面的参数传进去
        self.db.commit()
        return item

    # open_spider()和close_spider()：只在爬虫被打开和关闭时，执行一次。
    def open_spider(self, spider):
        self.db = mysql.connector.connect(host='localhost', user='root', port=3306, passwd='123456', db='xzlmark', charset='utf8')
        self.cursor = self.db.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
```

settings中的设置：

```python
ITEM_PIPELINES = {
'xicidailiSpider.pipelines.XicidailispiderPipeline': 300,
}
```



# response.follow 和scrapy.Resquest的区别

​	1、response.follow()支持相对地址，Request必须是绝对地址。

​	2、response.follow()可以使用选择器:

```python
	    for href in response.css('li.next a::attr(href)'):

​			yield response.follow(href,callback=selef.parse)

```

​	3、response.follow()还可以使用标签

```python
for a in response.css('li.next a'):

​			yield response.follow(a,callback=self.parse)
```



# 智能翻页及处理链接中的链接（思路）：

```python
import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']   #需要爬取的受首页

    def parse(self, response):
        # follow links to author pages   # 爬取主页面中的列表，同时还需要这个列表中其他链接的字段，可以在下面的回调函数中设置
        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href, self.parse_author)

        # follow pagination links
        for href in response.css('li.next a::attr(href)'):   # 这个是实现翻页的功能，回调解析函数本身
            yield response.follow(href, self.parse)

    def parse_author(self, response):
        def extract_with_css(query):   # 定义一个函数，可以方便下面使用，值得借鉴
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        }
```

# get()和extract()方法

![1560606713745](.\image\get-extract.png)

