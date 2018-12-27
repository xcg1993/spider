"""
selenium -> swith_to_frame(frame)
从iframe标签中查找元素
"""
import time

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://account.dianping.com/login?redir=http%3A%2F%2Fwww.dianping.com%2F')
iframe=driver.find_element_by_tag_name('iframe')
driver.switch_to.frame(iframe)
time.sleep(3)
span_login=driver.find_element_by_class_name('bottom-password-login')
if span_login:
    span_login.click()

time.sleep(10)
driver.quit()
