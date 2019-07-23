'''
功能：爬取好听轻音乐网（http://www.htqyy.com/）的音乐链接，保存到CSV文件中，可以用迅雷批量下载
分析：这类网站往往是把歌曲缓存在本地的，如果直接打开歌曲，我们还没来得及抓，就不见了。所以在首页中，
    我们随意打开一个大的分类，这里我打开热播榜，然后打开开发者工具进行抓包。
通过抓包得到：
    1.http://www.htqyy.com/top/musicList/hot?pageIndex=1&pageSize=20   这个是这个分类下歌曲的接口
    2.通过再次翻页，可以确定：pageIndex 和 pageSize 是可变参数，pageIndex是从0开始的，这个列别的歌曲就是通过这个接口进行加载的，而浏览器中的
        地址是不变的。
    3.通过右键点击任意一个歌曲，复制链接，然后在新窗口通过抓包可得，歌曲的信息是：http://f2.htqyy.com/play7/327/mp3/6 这个接口，通过
        多次验证，只有中间327的位置是可变的。
    4.通过第3的分析，然后倒转到2中查看，数字就是歌曲的id，在2的抓包中可以得到。
'''
import re
import requests
import os
import csv

class Htqyy(object):
    def __init__(self):
        self.url = 'http://www.htqyy.com/top/musicList/hot?pageIndex={}&pageSize=20'   # 翻页的链接
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }

    def get_music_title_link(self, path, filename, page):
        '''
        :param path: 文件保存目录
        :param filename: 文件名称，不需要添加后缀名
        :param page: 需要下载的页数（每页20条数据）
        :return:None
        '''
        for i in range(0, page):
            res = requests.get(self.url.format(i), headers=self.headers, timeout=10)
            # 用正则表达式提取歌曲title和ID,这样返回的是列表，中间是用元组形式存储的
            title_ids = self.__get_re_result(r'title="(.*?)" sid="(\d+)">', res.text)
            print(title_ids)
            # 下面这种形式叫序列解包
            for title, _id in title_ids:
                title = title.replace(',','-')  # csv默认逗号分隔，若标题中有英文逗号，则需要替换
                musci_link = f'http://f2.htqyy.com/play7/{_id}/mp3/6'
                items = f'{title},{musci_link}'
                self.__save_to_csv(path, filename, items)

    def __save_to_csv(self, path, filename, items):
        if os.path.exists(path) is False:
            os.makedirs(path)
        os.chdir(path)  # 如果目录在，则进入这个目录
        try:
            with open(filename+'.csv', 'a', newline='') as f:
                # writer =csv.writer(f, delimiter=',')
                # writer.writerow(items+'\n')
                f.write(items+'\n')
        except Exception as ex:
            print(ex)

    def __get_re_result(self, pattern, string):
        re_obj = re.compile(pattern)
        return re_obj.findall(string)


if __name__ == '__main__':
    dytt8 = Htqyy()
    dytt8.get_music_title_link('.', '好听轻音乐', 1)
