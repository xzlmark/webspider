# 下载学习强国首页中的一张图片
import requests
url ='https://boot-img.xuexi.cn/image/1004/59154280256406732806101004/b65ff7929b674e2bb4bc9104996125ef-2.jpg'
r = requests.get(url)
with open('xidada.png','wb') as f:
    f.write(r.content)