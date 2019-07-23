'''
r.content保存二进制内容、图片、歌曲、电影等,如果需要保存这类数据，就不能使用r.text，而要用r.content
'''
import requests
url ='https://www.baidu.com/img/bd_logo1.png'
r = requests.get(url)
# 保存图片,
with open('baidu.png','wb') as f:
    f.write(r.content)