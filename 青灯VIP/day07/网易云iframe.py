from selenium import webdriver

url = 'https://music.163.com/#/song?id=31108473'

driver = webdriver.Chrome()

driver.get(url)
# driver.switch_to.frame(0)  # 页面有iframe,需要切换，不然得不到数据,可以是index、name、ID、xpath定位到的元素
# driver.switch_to.frame('contentFrame')  # name
# driver.switch_to.frame('g_iframe')  # id
driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@id="g_iframe"]'))  # xpath定位元素
msg = driver.find_element_by_xpath('//div[@class="cnt f-brk"]')
print(msg.text)
driver.quit()