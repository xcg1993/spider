"""
http://www.meinv.hk/
"""
import random
import time

from selenium import webdriver




chrome=webdriver.Chrome()
chrome.get('http://www.meinv.hk/')
time.sleep(random.uniform(4,7))
js_script="""
var  d = document.documentElement.scrollTop=10000;
"""

js_script="""
var  load_more = document.getElementById('fa-loadmore');
load_more.click()
"""


chrome.execute_script(js_script)
chrome.find_element_by_xpath('//button[@id="fa-loadmore"]').click()
time.sleep(2)
chrome.execute_script(js_script)
# chrome.execute_async_script('alert("Hi，xcg");')
time.sleep(2)
chrome.quit()
