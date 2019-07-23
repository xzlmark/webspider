import requests
'''
免费代理网站：
    http://proxylist.fatezero.org/
    http://ip.zdaye.com/FreeIPList.html
    太阳
    芝麻代理 推荐
    阿布云
    蘑菇代理
'''
url = 'http://icanhazip.com/'
proxies = {
    'http':'139.99.73.185',
    'https':'189.204.158.161'
}
res = requests.get(url,proxies= proxies)
print(res.text)