from flask import Blueprint
from flask import render_template
from flask import request
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pyquery import PyQuery as pq

blue = Blueprint('first_blue', __name__)


@blue.route('/')
def index():
    return render_template('index.html')


@blue.route('/douyin/')
def douyin():
    douyin_type = request.values.get('type')
    driver = webdriver.Chrome()
    driver.get('https://www.newrank.cn/public/info/list.html?period=tiktok_day')
    driver.maximize_window()
    driver.implicitly_wait(3)

    driver.find_element_by_xpath(f'//div[@class="tiktok-right-type-list"]/span[{douyin_type}]').click()
    driver.execute_script('document.documentElement.scrollTop=800')
    time.sleep(1)
    driver.execute_script('document.documentElement.scrollTop=5000')
    driver.minimize_window()
    text = driver.page_source
    time.sleep(1)
    driver.quit()
    doc = pq(text)
    text = str(doc('.l_container'))
    return text


@blue.route('/weixin/')
def weixin():
    weixin = request.values.get('weixin')
    driver = webdriver.Chrome()
    driver.get('https://www.newrank.cn/')
    driver.implicitly_wait(3)
    driver.maximize_window()

    handle1 = driver.current_window_handle
    driver.find_element_by_id('txt_account').send_keys(weixin)
    driver.find_element_by_id('txt_account').send_keys(Keys.ENTER)
    # 扫码登录
    time.sleep(10)
    driver.minimize_window()
    lists = []  # 保存查找到的微信列表
    aticles_list = []  # 保存返回的文档列表
    try:
        lists = driver.find_elements_by_class_name('searchImg')
        # print(len(lists))
    except:
        print('没有这个微信号')
        return '这个微信号没有内容'
    for i in range(0, 3):
        try:
            lists[i].click()
            hsnds = driver.window_handles
            driver.switch_to.window(hsnds[-1])
            time.sleep(5)
            driver.execute_script("window.scrollTo(0,3000)")  # 0,0为顶部
            text = driver.page_source
            try:
                if '请耐心等待' not in text:  # 将没有内容的排除
                    # 将结果存为pyqury对象
                    doc = pq(text)
                    text = str(doc('.info-detail-article-top'))
                    aticles_list.append(text)
                    time.sleep(3)
                    driver.close()
                    driver.switch_to.window(handle1)
                else:
                    driver.close()
                    driver.switch_to.window(handle1)
            except:
                continue
        except:
            print('程序出错')
            return '没有此微信号内容'
    aticles=''
    driver.quit()
    for i in range(0, len(aticles_list)):
         aticles=aticles+aticles_list[i]
    return aticles