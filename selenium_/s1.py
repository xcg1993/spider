import time
from selenium.webdriver.chrome.options import Options

from selenium import  webdriver

#打开网页
from selenium.webdriver.remote.webelement import WebElement

options=Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
# options.binary_location=r'D:\chromedriver.exe'
# 创建chrome浏览器
browser=webdriver.Chrome()
# path=r'D:\chromedriver.exe'
browser.get('https://www.baidu.com')
time.sleep(3)
input_element:WebElement=browser.find_element_by_id('kw')
input_element.send_keys('斗鱼')      #设置搜索框内容
#查找搜索百度的button  id=su
button_su=browser.find_element_by_id('su')
button_su.click()#点击控件
time.sleep(5)
browser.save_screenshot('douyu.png')
browser.close()#关闭网页
browser.quit()#退出浏览器