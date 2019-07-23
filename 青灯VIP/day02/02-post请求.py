'''
网络请求的两种方式

'''

import  requests
# 拼接网址 format、%s、f格式
# url = 'https://www.sogou.com/web?' + 'query=scrapy'
# url ='https://www.sogou.com/web?{}'.format('query=scrapy')
# url = f'https://www.sogou.com/web?{"query=scrapy"}'
# response = requests.get(url)
# print(response.text)


#第二种方式，用params传递

url = 'https://www.sogou.com/web?'
param = {'query':'scrapy'}
res = requests.get(url,params=param)
res.encoding='utf-8'
print(res.text)