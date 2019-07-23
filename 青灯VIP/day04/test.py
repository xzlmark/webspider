import requests
import re

res = requests.get('http://proxylist.fatezero.org/proxy.list')
infos = res.text.split('\n')  # 将获取的内容换行
for info in infos:
    try:
        port = re.findall(r'"port": (\d+)', info)[0]
        ips = re.findall('(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', info)
        ips = list(set(ips))  # 每一行去重
        for ip in ips:
            print(':'.join(ip+port))
    except:
        pass




