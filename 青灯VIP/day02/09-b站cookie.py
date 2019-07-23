import requests
url ='https://account.bilibili.com/home/userInfo'
cookie = {
    'cookie':None
}
res = requests.get(url,cookies=cookie)
print(res.json())

'''
作业：B站弹幕发送

1、发送直播间弹幕
2、发送视频（别人上传的）弹幕
'''