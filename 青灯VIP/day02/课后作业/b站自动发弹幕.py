'''
功能：b站发送直播间弹幕，通过传递房间号和弹幕内容自动发送。通过抓包得到
1、发送信息的接口为：https://api.live.bilibili.com/msg/send
2、通过post方式发送
3、表单数据为：color: 16777215
                fontsize: 25
                mode: 1
                msg: 厉害
                rnd: 1561205589
                roomid: 21444317
                bubble: 0
                csrf_token: 74af7ba9db15e6d68e0185275259448c
                csrf: 74af7ba9db15e6d68e0185275259448c
4、要实现这个功能，只需要将相关内容传给request即可。
5、因为这个功能是需要登录后才能操作的，所以必须要将cookie内容也携带上
'''
import time
import requests
import json

def send_msg(roomid, msg):
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://live.bilibili.com',
        "Cookie": "sid=4zzwql59; buvid3=291931B6-3FFA-46B7-9D6B-A734BD87A40E40775infoc; LIVE_BUVID=AUTO1515611957852364; DedeUserID=437032110; DedeUserID__ckMd5=be00b14820563fe9; SESSDATA=61d3d131%2C1563787852%2C8f18c661; bili_jct=74af7ba9db15e6d68e0185275259448c; _dfcaptcha=cde4e058711f2d12a0544b301d7247fd; _uuid=B22482EE-7CA3-4224-08D7-2CCDE85382A602317infoc; UM_distinctid=16b7f397fc6328-0f8bf8bfb545da-3e385b04-1fa400-16b7f397fc7945; CNZZDATA2724999=cnzz_eid%3D1383005088-1561202886-https%253A%252F%252Fwww.bilibili.com%252F%26ntime%3D1561202886",
        'Referer': 'https://live.bilibili.com/166?visit_id=avgzu2em3o40',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    }
    data = {
        'color': '16777215',
        'fontsize': '25',
        'mode': '1',
        'msg': msg,
        'rnd': '1561207754',
        'roomid': roomid,
        'bubble': '0',
        'csrf_token': '74af7ba9db15e6d68e0185275259448c',
        'csrf': '74af7ba9db15e6d68e0185275259448c',
    }
    response = requests.post('https://api.live.bilibili.com/msg/send', data=data, headers=headers)
    # 判断是否发送成功
    if response.status_code == 200:
        print('发送成功')
    else:
        print('发送出错')

def get_msg(roomid):
    form_data = {
        'roomid': roomid,
        'csrf_token': '74af7ba9db15e6d68e0185275259448c',
        'csrf': '74af7ba9db15e6d68e0185275259448c',
        'visit_id': '',
        'data_behavior_id': '14d0f0cb3b208d',
        'data_source_id': 'system',
    }
    res = requests.post('https://api.live.bilibili.com/ajax/msg', data=form_data)
    infos = json.loads(res.text)
    return  [info['text'] for info in infos['data']['room']]


if __name__ == '__main__':
    # 输入房间号 4791641
    roomid = input('请输入房间号：')
    contents = get_msg(roomid)
    for content in contents:
        time.sleep(3)
        send_msg(roomid, content)
