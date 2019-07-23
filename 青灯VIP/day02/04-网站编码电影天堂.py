import requests

url ='https://www.dytt8.net/'
response = requests.get(url)
# 默认的是什么编码
print(response.encoding)

# 乱码就去网站看是什么编码信息，然后通过下面的方式修改
response.encoding = 'gb2312'
