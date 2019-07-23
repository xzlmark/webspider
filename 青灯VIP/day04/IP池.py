'''
IP池：存储ip的池子，一般是Redis、MongoDB
IP设计时要考虑的问题：
    1、IP的来源，免费或收费都行
    2、IP检测问题，要定期检测I值，剔除不能使用的
    3、提供外部调用，让爬虫程序能使用IP

proxy_pool代理池
APScheduler：定时模块
'''
import requests

res = requests.get('http://localhost:5010/get',timeout=10)
print(res.text)
proxies = {
    'http':res.text,
    'https':res.text
}
res = requests.get('http://icanhazip.com/',proxies= proxies)
print(res.text)