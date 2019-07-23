# 通过Python程序爬取豆瓣网站Top250电影页面，将电影的信息保存到CSV文件中

import re
import os
import csv
import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}


def get_movie_details_links(pages):
    for page in range(0, pages):
        url = f'https://movie.douban.com/top250?start={page * 25}&filter='
        response = requests.get(url, headers=headers)
        response.encoding = 'utf8'
        detail_links = re.findall('<a href="(.*?)" class="">', response.text)
        return detail_links


def get_movie_data(path, filename, detail_links):
    '''
    :param path:保存文件的路径
    :param filename:文件名称，不需要后缀名
    :param detail_links:电影详情页链接，列表格式
    :return:
    '''
    for detail_link in detail_links:
        response = requests.get(detail_link, headers=headers)
        response.encoding = 'utf-8'
        res = response.text
        title = re.findall('<span property="v:itemreviewed">(.*?)</span>', res)[0]        # 电影名称
        year = re.search('<span class="year">(.*?)</span>', res).group(1)   # 电影中的年份
        title = title + year  # 电影名称+年份
        pic = re.search('<img src="(.*?)" title="点击看更多海报"', res).group(1)          # 图片
        score = re.search('property="v:average">(.*?)</strong>', res).group(1)          # 评分
        numbers = re.search('<span property="v:votes">(.*?)</span>', res).group(1)         # 评价人数
        # 电影简介,简介中包括需要展开的和不需要展开的两种情况，因为列表可能会报错，需要try
        try:
            if '展开全部' in res:
                brief = re.search('<span class="all hidden">(.*?)</span>', res, flags=re.S).group(1).strip()  # 去掉首尾的空格
            else:
                brief = re.search('<span property="v:summary" class="">(.*?)</span>', res, flags=re.S).group(1).strip()
            brief = re.sub(r'<br />', '', brief)  # 把简介中的<br />去掉
            brief = re.sub(r'\s', '', brief)  # 把简介中的空白字符去掉
        except Exception as ex:
            print(ex)
            brief = ''
        # 返回列表形式，CSV可以用字符串或列表写入
        save_to_file(path, filename, [title, score, numbers, pic, brief])


# 将列表数据保存到硬盘中，格式CSV
def save_to_file(path, filename, items):
    # 传入的路径是否存在，不存在则创建，存在则进入
    if os.path.exists(path) is False:
        os.makedirs(path)
    else:
        os.chdir(path)
    with open(filename+'.csv', 'a', encoding='gb18030', newline='') as f:   # 这里用utf-8乱码
        writer = csv.writer(f)
        writer.writerow(items)


if __name__ =='__main__':
    links = get_movie_details_links(1)
    get_movie_data('.', 'douban', links)


