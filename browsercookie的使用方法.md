# browsercookie的使用方法

## 一、如果不适用scrapy的操作方式：   

```python
 cookiejar = browsercookie.chrome() #或则firefox()
 requests.get(url,cookies = cookiejar)即可实现
```

## 二、使用scrapy,可以要在下载中间件中自定义cookie中间件

​    1、在settings中设置COOKIES_ENABLED = True
​    2、启用DOWNLOADER_MIDDLEWARES = {
​        'scrapy.downloadermiddlewares.cookies.CookiesMiddleware':None,  #关闭
​         'browser_cookie.middlewares.BrowserCookiesMiddleware': 1,
​        }
​    3、在middleware中编写中间件，需要继承scrapy的CookiesMiddleware类     

```python
   class BrowserCookiesMiddleware(CookiesMiddleware):
        def __init__(self,debug=False):  # 重写父类的构造方法，将浏览器cookie存入jar中
        super().__init__(debug)
        self.load_browser_cookies()

​        def load_browser_cookies(self):
            jar = self.jars['chrome']  #chrome就是键，在request时，传入meta的时候需要使用
            chrome_cookiejar = browsercookie.chrome()
            for cookie in chrome_cookiejar:
               jar.set_cookie(cookie) # 加载Chrome浏览器中的cookie
```

## 三、如何使用：

​    如果要爬虫开始就请求需要登录后才能操作的页面，则需要在spider的start_requests中重写方法,这里必须用yield，回调函数默认为parse        

```python
		def start_requests(self):
             yield scrapy.Request('https://kyfw.12306.cn/otn/view/index.html',meta={'cookiejar':'chrome'})
```

​    在spider中如果还需要继续使用，则可以直接调用scrapy.Request(url,meta={'cookiejar':'chrome'})即可

## 四、如果在spider中需要访问request和response中的cookie，使用下面的方法

​    cookie = response.request.headers.getlist('Cookie')
​    cookie1 = response.headers.getlist('Set-Cookie')