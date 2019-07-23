import requests

# 用requests的headers添加请求头
url = 'https://www.baidu.com/s?wd=scrapy'
ua = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1'
}
res = requests.get(url, headers=ua)
print(res.text)
# 有时候加上了UA，但是还是无法访问，可能还需要添加下面的内容：  referer、host、cookie