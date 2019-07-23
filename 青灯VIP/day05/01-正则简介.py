import re

pattern = '\d+'   # 正则表达式
string = 'fsdjfsjfsd354dfsdfsd5'
result = re.search(pattern, string)  # search只搜索一次
print(result)  # 返回的结果为：<re.Match object; span=(10, 13), match='354'>。span 是匹配的位置，match是匹配的值
# 强烈注意：文件起名字的时候，千万不要用re来作为名字
