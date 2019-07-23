from fake_useragent import UserAgent
import time,random

ua = UserAgent()  # 实例化
print(ua.random)    # #随机打印任意厂家的浏览器
print(ua.ie)  # 随机打印ie浏览器任意版本
print(ua.chrome)
print(ua.firefox)

# 15621609615692
# 15621689748231
# 1562168915756
# 1562168722034
# 1562168742240
salt = str(int(round(time.time() * 1000)))+str(random.randint(0, 10))
print(salt)