'''
爬虫生产者与消费者
    1、先有网址队列（生产者）
    2、采集线程（消费者）（同时生产源码）
    3、源码队列
    4、提取线程（消费者 消费网页源码）
    5、保存数据
'''
import queue
import threading

import requests


# 准备网址
def prepare_url_queue():
    '''
    准备网址队列
    :return: 网址队列
    '''
    url_queue = queue.Queue()
    for start in range(0,250,25):
        url = f'https://movie.douban.com/top250?start={start}&filter='
        url_queue.put(url)
    return url_queue


class CrawlThread(threading.Thread):
    def __init__(self, name,url_queue=None):
        super(CrawlThread,self).__init__(name=name)
        self.url_queue = url_queue
        # 初始化网址

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
        # 取出网址，发出请求
        while not self.url_queue.empty():
            try:
                url = self.url_queue.get(block=False)
                print(f'当前线程是{self.name}--->{url}')
                response = requests.get(url,headers = headers)
                response_queue.put(response)
            except:
                pass


class ParseThread(threading.Thread):
    def __init__(self, name,response_queue=None):
        super(ParseThread,self).__init__(name=name)
        self.response_queue = response_queue
        # 初始化网址

    def run(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.75 Safari/537.36'
        }
        # 取出网址，发出请求
        while not self.url_queue.empty():
            try:
                url = self.url_queue.get(block=False)
                print(f'当前线程是{self.name}--->{url}')
                response = requests.get(url,headers = headers)
                response_queue.put(response)
            except:
                pass

if __name__ == '__main__':
    print('主线程开始')
    url_queue = prepare_url_queue()
    # 网页源码队列
    response_queue = queue.Queue()
    crawl_threds = []
    for i in range(4):
        crawl_thred = CrawlThread(f'采集线程{i}', url_queue = url_queue)
        crawl_threds.append(crawl_thred)
    for target in crawl_threds:
        target.start()
    for target in crawl_threds:
        target.join()

    print('主线程结束')
