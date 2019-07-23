'''
要求：豆瓣Top250数据提取  
		采集网址：https://movie.douban.com/top250 
		采集目标：剧情简介 电影名称 电影图片 电影评分  评价人数
		采集要求：
			* 必须使用XPath来提取数据
			* 必须使用函数式编程 尽量使用面向对象式编程
			* 数据必须保存到CSV文件
分析：此网站通过抓包工具分析，数据是通过下面接口传递的，是get请求。
        https://movie.douban.com/top250
    参数是：
    start: 0
    filter:
'''

import re
import requests
import csv
from lxml import etree


def get_data(page):
    '''
    :param page: 需要下载多少页
    :return: 返回list数据
    '''
    url = 'https://movie.douban.com/top250'
    data = {
        'start': (page-1)*25,
        'filter': ''
        }
    res = requests.get(url,params = data)
    if res.status_code == 200:
        html = etree.HTML(res.text)
        # 电影所有信息
        infos = html.xpath('//ol[@class="grid_view"]')
        for info in infos:
            # 电影名称
            name = info.xpath('.//span[@class="title"][1]/text()')
            # 剧情简介
            profile = info.xpath('//span[@class="inq"]/text()')
            # 电影评分
            score = info.xpath('.//span[@class="rating_num"]/text()')
            # 评价人数
            numbers = info.xpath('.//div[@class="star"]/span[4]/text()')
            # 电影图片
            pic = info.xpath('.//div[@class="pic"]/a/@href')
            for name,profile,score,numbers,pic in zip(name,profile,score,numbers,pic):
                # 把‘人评价’替换
                numbers = re.sub('人评价', '', numbers)
                yield [name,profile,score,numbers,pic]
            
            
def save2csv(items):
    for item in items:
        with open('movie.csv','a',newline='',encoding='gb18030') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(item)

        
if __name__ == '__main__':
    # 初始化CSV文件
    with open('movie.csv','a',newline='',encoding='gb18030') as f:
        title = ['电影名称','剧情简介','电影评分','评价人数','电影图片']
        f_csv = csv.writer(f)
        f_csv.writerow(title)
    for page in range(1, 11):  # 下载10页数据
        items = get_data(page)
        save2csv(items)
