'''
下载飘花电影的信息保存在文件中
地址：https://www.piaohua.com/html/dongzuo/index.html
'''
import requests

url = 'https://www.piaohua.com/html/dongzuo/'

for page in range(1, 6):
    res = requests.get(url+'list_%s.html' % page)
    with open('./movie/page{0}.html'.format(page), 'wb') as f:
        f.write(res.content)