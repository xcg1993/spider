# -*- coding: utf-8 -*-
import scrapy


class XiaohuameinvSpider(scrapy.Spider):
    name = 'xiaohuameinv'
    allowed_domains = ['www.521609.com']
    start_urls = ['http://www.521609.com/daxuexiaohua/list32.html']

    def parse(self, response):
        pass
