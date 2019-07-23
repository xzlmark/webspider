from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.baidu.com')
cookie = driver.get_cookies()  # 获取的是访问本网站的cookie

print(len(cookie))

driver.quit()
