'''
用正则表达式提取电影天堂的电影链接
要求，实现翻页（for循环）、提取详情页的网址，下载详情页中的电影名称及下载链接，保存到csv文件
'''
import os
import re
import requests


class Dytt8(object):
    def __init__(self):
        self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'   # 翻页的链接
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def get_title_downloadlink(self, path, filename, page):
        '''
        :param path: 文件保存目录
        :param filename: 文件名称，不需要添加后缀名
        :param page: 需要下载的页数（每页25条数据）
        :return:None
        '''
        for i in range(1, page+1):
            res = requests.get(self.url.format(i), headers=self.headers, timeout=10)
            res.encoding = 'gb18030'
            # 用正则表达式提取详情页的链接,这个链接是相对路径，需要拼接 /html/gndy/dyzz/20190625/58766.html
            detail_links = self.__get_re_result('<a href="(.*?)" class="ulink">',res.text)
            for detail_link in detail_links:
                res = requests.get('https://www.dytt8.net/'+detail_link, headers=self.headers, timeout=10)
                res.encoding = 'gb18030'
                # 找到电影标题,只有一个，findall结果为列表
                dolownd_title = self.__get_re_result('<h1><font color=#07519a>(.*?)</font></h1>', res.text)[0]
                # 找到电影下载链接
                download_link = self.__get_re_result('<a href="(.*?)">ftp', res.text)[0]
                items = f'{dolownd_title},{download_link}'   # csv格式是用,分割的
                self.__save_to_csv(path, filename, items)

    def __save_to_csv(self, path, filename, items):
        if os.path.exists(path) is False:
            os.makedirs(path)
        os.chdir(path)  # 如果目录在，则进入这个目录
        try:
            with open(filename+'.csv', 'a') as f:
                f.write(items+'\n')
        except Exception as ex:
            print(ex)

    def __get_re_result(self, pattern, string):
        re_obj = re.compile(pattern)
        return re_obj.findall(string)


if __name__ == '__main__':
    dytt8 = Dytt8()
    dytt8.get_title_downloadlink('.', '电影天堂', 2)

