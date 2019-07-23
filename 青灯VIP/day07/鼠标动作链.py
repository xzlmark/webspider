'''


'''
import time
from selenium import webdriver

from selenium.webdriver import ActionChains  # 导入鼠标动作链

driver = webdriver.Chrome()
driver.get('http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
driver.switch_to.frame('iframeResult')
drag = driver.find_element_by_id('draggable')
drop = driver.find_element_by_id('droppable')
# 实例化鼠标动作链,把浏览器对象作为参数
action = ActionChains(driver)
action.drag_and_drop(drag,drop)
action.perform()  # 执行动作链，不然不会执行
time.sleep(5)
driver.quit()