# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy.http import Response


class HotSpider(scrapy.Spider):
    name = 'hot'
    allowed_domains = ['www.jokeji.cn']
    start_urls = ['https://www.jokeji.cn/hot.asp?me_page=1']

    def parse(self, response:Response):
        if response.status==200:
            a_list=response.xpath('//a[@class="main_14"]')    #[<Selector>]
            for a in a_list:
                href='http://www.jokeji.cn'+a.xpath('@href').extract()[0]
                title=a.xpath('text()').extract()[0]
                yield Request(href,callback=self.parse_content,meta={'title':title})

    def parse_content(self,response:Response):
        if response.status==200:
            contents=response.xpath('//*[@id="text10"])//font/text()').extract()
            title=response.meta.get('title')
            return {
                'title':title,
                'contents':contents
            }
