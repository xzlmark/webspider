'''
要求：腾讯招聘 数据获取 
		采集网址：https://careers.tencent.com/search.html
		采集目标：职位名字 职位简介 工作职责 工作要求 
		采集要求：
			* 必须使用XPath来提取数据
			* 数据必须保存到CSV文件 
分析：此网站通过抓包工具分析，数据是通过下面接口传递的，是get请求。
        https://careers.tencent.com/tencentcareer/api/post/Query
    参数是：
    timestamp: 1562051441303
    countryId: 
    cityId: 
    bgIds: 
    productId: 
    categoryId: 
    parentCategoryId: 
    attrId: 
    keyword: 
    pageIndex: 3
    pageSize: 10
    language: zh-cn
    area: cn

'''
import requests
import csv
import time

def get_postId(page):
    '''
    page :需要下载的页数,每页默认为20，参数可改
    '''
    # 获取列表页的网址接口
    url = 'https://careers.tencent.com/tencentcareer/api/post/Query'
    current_milli_time = lambda: int(round(time.time() * 1000))
    data = {
        'timestamp': current_milli_time,
        'countryId':'',
        'cityId':'',
        'bgIds': '',
        'productId': '',
        'categoryId': '',
        'parentCategoryId': '',
        'attrId': '',
        'keyword': '',
        'pageIndex': page,
        'pageSize': 20,
        'language': 'zh-cn',
        'area': 'cn',
        }
    infos = requests.get(url,params = data).json()
    for info in infos['Data']['Posts']:
        _id = info['PostId']
        yield _id

def get_data(_id):
    url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId'
    data = {
        'timestamp': lambda: int(round(time.time() * 1000)),
        'postId': _id,
        'language': 'zh-cn'
        }
    res = requests.get(url,params = data)
    infos = res.json()
    info = infos['Data']
    postname = info['RecruitPostName']  # 岗位名称
    responsibility = info['Responsibility']  # 工作职责
    req = info['Requirement']  # 工作要求
    # 简介
    profile = info["BGName"]+'|'+info["LocationName"]+'|'+info["CategoryName"]+'|'+info["LastUpdateTime"]
    return [postname,profile,responsibility,req]

def save2csv(items):
    with open('result.csv','a',newline='',encoding='gb18030') as f:
        f_csv = csv.writer(f)
        f_csv.writerow(items)

        
if __name__ == '__main__':
    # 初始化CSV文件
    with open('result.csv','a',newline='',encoding='gb18030') as f:
        title = ['职位名称','职位简介','工作职责','工作要求']
        f_csv = csv.writer(f)
        f_csv.writerow(title)
    for page in range(1,3):
        ids = get_postId(page)
        for _id in ids:
            items = get_data(_id)
            save2csv(items)
