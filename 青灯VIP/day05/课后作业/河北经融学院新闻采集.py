'''
功能：采集河北金融学院的新闻，地址为：https://www.hbfu.edu.cn/news/queryListForPage
分析，通过抓包：
    得到新闻列表的接口为：https://www.hbfu.edu.cn/news/queryListForPage   post模式,form数据为：start: 20  limit: 20  type: 1。
    其中type、limit 不变;start从0开始，20为步长进行增长。
新闻详情页的接口为：https://www.hbfu.edu.cn/news/findById  post方式，form表单数据为id，ID就是新闻的ID号，通过进一步分析，
    并查看新闻列表中返回的json数据中就包括了新闻标题。

'''
import requests
import re


# 这个函数是给定需要下载的页码，下载所有新闻的标题和内容，并存在当前目录下，格式CSV文件
def get_news_title_content(page):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                        Chrome/75.0.3770.100 Safari/537.36',
    }
    for i in range(0, page):
        form_data = {'start': (i * 20),'limit': 20,'type': 1}
        res = requests.post('https://www.hbfu.edu.cn/news/queryListForPage', data=form_data, headers=headers, verify=False)
        print(res.text)
        infos = res.json()
        for info in infos['rows']:
            _id = info['id']
            print(_id)
            infos = requests.post('https://www.hbfu.edu.cn/news/findById', data={'id': _id}, headers=headers, verify=False).json()
            title = infos['title']
            contents = infos['content']
            # 通过正则表达式提取正文内容
            contents = re.findall(r'style="text-indent:2em;">\r\n\t(.*?)\r\n</p>\r\n', contents, re.S)
            content = ''.join(contents)  # 将列表中的内容保存为字符串格式
            items = f'{title},{content}'  # 构造用逗号分隔的字符串
            save_to_csv(items)


# 将文件保存在当前目录下，参数为每行写入的字符串
def save_to_csv(items):
    with open('news.csv', 'a', newline='') as f:
        f.write(items+'\n')


if __name__ == '__main__':
    get_news_title_content(5)
