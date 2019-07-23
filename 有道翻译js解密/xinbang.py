import math, random
import requests
import browsercookie

'''
for (var a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"], b = 0; b < 500; b++) for (var c = "",
        d = 0; d < 9; d++) {
            var e = Math.floor(16 * Math.random());
            c += a[e]
        }
这个无法运行，未修正
'''


def get_nonce():
    a = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f"]
    c = ''
    for i in range(0, 9):
        b = math.floor(16 * random.random())
        c += a[b]
    print(c)
    return c


'''
i += "&nonce=" + j,   j 就是上面的nonce
'''


def get_xzy(nonce):
    import hashlib
    md5 = hashlib.md5()
    xyz = '&nonce=' + nonce
    md5.update(xyz.encode('utf-8'))
    return md5.hexdigest()


def get_data(weixin):
    '''
    filter: 
    hasDeal: false
    keyName: 范冰冰
    order: relation
    nonce: 903ae515b
    xyz: a2e23ef3362c8e341148a64084386c1b
    '''
    nonce = get_nonce()
    xyz = get_xzy(nonce)
    print(xyz)
    url = 'https://www.newrank.cn/xdnphb/data/weixinuser/searchWeixinDataByCondition'
    data = {
        'filter': '',
        'hasDeal': 'false',
        'keyName': weixin,
        'order': 'relation',
        'nonce': nonce,
        'xyz': xyz,
    }
    print(data)
    cookies = browsercookie.chrome()
    resonse = requests.post(url, data=data, cookies=cookies)
    if resonse.status_code == 200:
        print(resonse.text)
    else:
        print('请求错误')


if __name__ == '__main__':
    get_data('范冰冰')
