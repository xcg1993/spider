"""
https://sou.zhaopin.com/?jl=854&kw=python%E8%BF%90%E7%BB%B4&kt=3
"""
import time
from threading import Thread

from bs4 import BeautifulSoup, Tag
from selenium import webdriver

from utils.mongo import db


class ZhaoPinSpider(Thread):
    def __init__(self):
        super().__init__()
        self.driver=webdriver.Chrome()
        #西安地区    kw是搜索的岗位名称
        self.url='https://sou.zhaopin.com/?jl=854&kw=%s&kt=3'



    def start_spider(self):
        #搜索关键字
        for kw in ('python','java','html'):

            yield(self.url % kw,self.parse)

    def parse(self,html):
        soup=BeautifulSoup(html,'lxml')
        divs=soup.select('.contentpile__content__wrapper_item')
        for div in divs:
            a:Tag=div.find('a')
            job_href=a.get('href')
            span=a.find('span',class_='contentpile__content__wrapper__item__info__box__jobname__title')

            job_name=span.text
            company_a=a.find('a',class_='company_title')
            company_name=company_a.text     #公司名称
            salary_p=a.find('p',class_='contentpile__content__wrapper__item__info__box__job saray')
            salary=salary_p.text
            job_demand_lis=a.find_all('li',class_='contentpile__content__wrapper__item__info__box__job__demand__item')
            job_demand=[li.text for li in job_demand_lis]   #工作位置，年限，学历要求
            self.item_pipeline(**{
                'job':job_name,
                'company':company_name,
                'salary':salary,
                'demand_region':job_demand[0],
                'demand_years':job_demand[1],
                'demand_xl':job_demand[2],
                'href':job_href


            })
    def download_middle(self,url,callback):
        self.driver.get(url)
        time.sleep(3)
        html=self.driver.page_source
        callback(html)
        # div=self.driver.find_elements_by_class_name('soupager')[0]
        # next_btn=div.find_element_by_xpath('./button[2]')
        # print(next_btn.text)
        # for btn in next_btn:
        #     if btn.text=='下一页'and btn.is_enabled():
        #         btn.click()
        #         time.sleep(5)
        #         html = self.driver.page_source
        #         callback(html)
    def run(self):
        print('--启动爬虫--')
        for url,callback in self.start_spider():
            print(f'--开始下载{url}--')
            self.download_middle(url,callback)
    def item_pipeline(self,**data):
        #将数据写入到mongodb中
        print(data)
        db.jobs.insert(data)
    def __del__(self):
        self.driver.close()
        self.driver.quit()
if __name__ == '__main__':
    spider=ZhaoPinSpider()
    spider.start()
    spider.join()
    print('over')