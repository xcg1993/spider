# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class GendySpider(scrapy.Spider):
    name = 'gendy'
    allowed_domains = ['www.dytt8.net']
    start_urls = ['https://www.dytt8.net/html/gndy/dyzz/index.html/']

    def parse(self, response):
        #找出下一页的href
        base_href='https://www.dytt8.net/html/gndy/dyzz/'
        next_a=base_href+response.css('.x').xpath('.//a/@href').extract()[-2]
        print(next_a)

        #response.css() 返回selectorlist   可迭代的
        links=[('https://www.dytt8.net'+ulink.xpath('@href').extract()[0],ulink.xpath('text()').extract()[0]) for ulink in response.css('.ulink')]
        for link,title in links:
            yield Request(link,callback=self.parse_info,
                          meta={'title':title})
        if next_a:
            yield Request(next_a)
    def parse_info(self,response):
        data={}
        texts=response.css('#Zoom p::text').extract()   #处理数据，提取各个特征字段
        if texts:
            data['name']=texts[0]
            data['zh_name']=texts[2]
            data['en_name'] = texts[3]
            data['year'] = texts[4]
            data['location'] = texts[5]
            data['lb'] = texts[6]
            y_name=texts[2].replace('\u3000','')
            data['imgs']=response.css('#Zoom img::attr(src)').extract()#第一个是海报，第二个是电影情节截图
            data['video_ftp']=response.xpath('//td[@style="WORD-WRAP:break-word"]/a/text()').extract()
            return data

