import requests
url = 'https://www.sogou.com/'

response = requests.get(url)

# response 得到的是网页中的源码格式，是html格式，与实际显示的有时并不一样，这点要注意
print(response.text)