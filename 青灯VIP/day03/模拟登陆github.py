'''
模拟登陆GitHub，案例分析：
    1、登陆往往会经过不同的请求，例如：验证码、帐号、密码
    2、登陆的时候基本为post操作
    3、登陆往往伴随验证码
    4、https://github.com/login 登陆的界面，里面是post表单登陆
    5、抓包写错误密码 不然登陆进去就不好抓了
    6、找但表单数据进行模拟登陆
    7、authenticity_token可以在网页中得到
'''
import requests
from bs4 import BeautifulSoup
# 先获取authenticity_token的网址，找到token的值
session = requests.session()   # 这里好像只能通过session才能成功登陆
url = 'https://github.com/session'
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}
# 发送请求
response = session.get(url, headers=headers)
# 找到token的值
soup = BeautifulSoup(response.text, 'lxml')
token = soup.find('input', {'name': 'authenticity_token'})['value']

# 发送请求，构造表单数据
post_url = 'https://github.com/session'
form_data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': token,
    'login': 'xzlmark@126.com',
    'password':'zlhyysxf781010',
    'webauthn-support': 'supported'}
res = session.post(post_url, data=form_data, headers=headers)
if 'xzlmark' in res.text:  # 通过用户名是否在返回的页面中判断是否登录成功
    print('登陆成功！！！！')
