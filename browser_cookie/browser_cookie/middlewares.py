# -*- coding: utf-8 -*-
import browsercookie
from scrapy.downloadermiddlewares.cookies import CookiesMiddleware


# cookie 中间件
class BrowserCookiesMiddleware(CookiesMiddleware):
    def __init__(self,debug=False):
        super().__init__(debug)
        self.load_browser_cookies()

    def load_browser_cookies(self):
        # 加载Chrome浏览器中的cookie
        jar = self.jars['chrome'] # jar属性是CookiesMiddleware中的属性
        chrome_cookiejar = browsercookie.chrome()
        for cookie in chrome_cookiejar:
            jar.set_cookie(cookie) # 将每个cookie存入jar中

        # 加载火狐浏览器
        # jar = self.jars['firefox']
        # firefox_cookiejar = browsercookie.firefox()
        # for cookie in firefox_cookiejar:
        #     jar.set_cookie(cookie)