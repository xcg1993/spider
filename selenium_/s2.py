"""
https://www.shailema.com/views/home/hall-show.html
"""
import re
import time

from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.remote.webelement import WebElement

chrome=webdriver.Chrome()



def start_spider():
    start_url='https://www.shailema.com/views/home/hall-show.html'
    download_middle(start_url,parse_mt)
def download_middle(url,callback):
    chrome.get(url)#会阻塞到网页请求完成
    html=chrome.page_source#获取网页内容
    callback(html)#可以考虑异步方式
    for _ in range(10):
        renovate:WebElement=chrome.find_element_by_class_name('renovate')
        renovate.click()
        callback(chrome.page_source)
        time.sleep(5)
def parse_mt(html):
    soup=BeautifulSoup(html,'lxml')
    model_items=soup.select('.modelItem')
    for model_item in model_items:
        a=model_item.find('a')
        detail_href='https://www.shailema.com/'+a.get('href')
        img_src='https://www.shailema.com'+a.find('img').get('src')[5:]
        info_ps=model_item.find('div',class_='informationBox').select('p')
        info=[]
        for info_p in info_ps:
            info.append(info_p.text.split('：')[-1])
        height,weight,age,city=tuple(info)
        name_p=model_item.find('p',class_='name')
        name=name_p.text
        sex_src=name_p.find('img').get('src')
        sex='女' if sex_src.find('boy') ==-1 else '男'

        item_pipeline(**{
            'city':city,
            'name':name,
            'sex':sex,
            'age':re.search(r'\d+',age).group(),
            'height':height,
            'weight':weight,
            'detail_href':detail_href,
            'img_src':img_src

        })
        # print(detail_href,img_src,height,weight,age,city)
def item_pipeline(**data):
    print(data)

if __name__ == '__main__':
    start_spider()