'''
功能：通过抓包，实现自动登录美食杰
通过抓包，可以看到：
    登录的地址为：https://i.meishi.cc/login.php
    查询的参数为：http://i.meishi.cc/    这个参数应该是登录成功后重定向的网页
    携带的表单数据为：
        redirect: https://www.meishij.net/     这个是重定向的网页，经过试验，正常登录后跳转的不是这个网页，
                                                是http://i.meishi.cc/，所以在传递参数的时候需要更改
        username: 18228647002
        password: 123456
这是一个简单的没有验证码等的登录，直接实现如下
'''
import requests

url = 'https://i.meishi.cc/login.php'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
}
data = {
        'redirect': 'http://i.meishi.cc/',
        'username': '18228647002',
        'password':  'XXXX'
}
res = requests.post(url, data=data, headers=headers)
if '杰米13863340' in res.text:
    print('登录成功')
else:
    print(res.text)
