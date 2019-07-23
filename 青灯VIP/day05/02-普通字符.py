'''
普通字符包括：大小写字母、数字等
'''

import re
pattern = 'Python'
string = 'I Love Python 666 888'
result = re.search(pattern,string) # search从左到右匹配，提取第一匹配的字符串
print(result.group())