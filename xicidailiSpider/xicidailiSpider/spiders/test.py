
if __name__=='__main__':
    import requests
    PROXY_POOL_URL = 'http://localhost:5000/get'
    response = requests.get(PROXY_POOL_URL)
    if response.status_code == 200:
        print(response.text)
    else:
        print('代理池连接失败....')