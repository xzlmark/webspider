# coding:utf-8

# 破解js加密，版本2
'''
一、先通过抓包工具得到js，然后在http://tool.oschina.net/codeformat/js中格式化js，再保存到编辑代码工具中备查。
二、通过抓包工具，得到如果需要得到翻译的接口，需要用到的请求参数为：
    i: 熊珍龙
    from: AUTO
    to: AUTO
    smartresult: dict
    client: fanyideskweb
    salt: 15621609615692
    sign: 13ab30cf4e960fba52d843cbadc7bf1f
    ts: 1562160961569
    bv: 6463522ba46bac94c96fd37965fadc8d
    doctype: json
    version: 2.1

三、通过测试，必须知道salt、sign、ts、by等4个参数。
四、通过在js文件中查找salt可以找到计算salt的公式
    salt=i = "" + (new Date).getTime()+  parseInt(10 * Math.random(), 10);

五、通过查找，sign定义如下：
    sign: n.md5("fanyideskweb" + e + i + "@6f#X3=cCuncYssPsuRUE")
    其中：md5有四个参数，第一个、第四个都是固定的，i就是前面的salt。还需要找到e、n。通过查找：
    n = e("./jquery-1.7"); 说明n、e就是需要翻译的字符串(输入的需要翻译的单词)
六、通过查找，ts定义如下：也就是salt不加后面随机的末尾数即可
    ts:r = "" + (new Date).getTime()

七、bv参数，定义如下：
    bv: t = n.md5(navigator.appVersion),这个应该是将浏览器的版本信息进行加密：5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 \
                    (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36。这里其实也可以就用默认的，因为一般请求不变
'''

import time, random
import requests
import hashlib


def get_ts():
    ts = str(int((time.time() * 1000)))
    return ts


def get_salt():
    ts = get_ts()
    salt = str(ts) + str(random.randint(0, 10))
    return salt


def getmd5(v):
    md5 = hashlib.md5()
    md5.update(v.encode('utf-8'))
    sign = md5.hexdigest()
    return sign


def getSign(key, salt):
    sign = "fanyideskweb" + str(key) + str(salt) + "@6f#X3=cCuncYssPsuRUE"
    sign = getmd5(sign)
    return sign


def youdao(kw, salt, ts):
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": kw,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(kw, salt),
        "ts": ts,
        "bv": "6074bfcb52fb292f0428cb1dd669cfb8",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTIME",
    }
    headers = {

            "Host": "fanyi.youdao.com",
            # "Proxy-Connection":"keep-alive",
            "Content-Length": str(len(data)),
            "Accept": "application/json, text/javascript, */*; q=0.01",
            "Origin": "http://fanyi.youdao.com",
            "X-Requested-With": "XMLHttpRequest",
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
            "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
            "Referer": "http://fanyi.youdao.com/",
            "Accept-Encoding": "gzip, deflate",
            "Accept-Language": "zh-CN,zh;q=0.9",
            "Cookie": "OUTFOX_SEARCH_USER_ID=119019685@10.168.8.63; JSESSIONID=aaaAioBu8RNDK46QQgoKw; \
            OUTFOX_SEARCH_USER_ID_NCOO=585978009.1173552; UM_distinctid=1690e1aeb4938-0e3d396c4bdd96-551f3c12-\
            100200-1690e1aeb4b7e; ___rl__test__cookies=1550723437154",
    }
    result = requests.post(url=url, data=data, headers=headers, timeout=10)
    res = result.json()
    print(res['translateResult'][0][0]['tgt'])


if __name__ == '__main__':
    src = input('请输入需要翻译的内容：')
    salt = get_salt()
    ts = get_ts()
    youdao(src, salt, ts)
