# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class GuoxueSpider(CrawlSpider):
    name = 'guoxue'
    allowed_domains = ['www.dushu.com']
    start_urls = ['https://www.dushu.com/guoxue/1001.html']

    rules = (
        #true表示针对提取的link下载并解析之后，会继续提取相关的规则；False，则在解析之后，不在继续提取
        #RULE()可以不用设置callback，表示只提取连接（parse），不解析下载后的数据
        Rule(LinkExtractor(allow=r'/guoxue/\d+/'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_css='.pages'), follow=True),  #下一页
    Rule(LinkExtractor(r'https://www.dushu.com/guoxue/\d+\.html'), follow = True)
    )


    def parse_item(self, response):
        #解析图书的详情页面
        i = {}
        i['book-title']=response.css('.book-title').xpath('h1/text()').extract()
        i['image']=response.css('.pic').xpath('img/@src').extract()[0]
        i['author']=''.join(response.css('.book-details-left').xpath('.//tr[1]/td[2]//text()').extract())
        #提取规则
        chaptor_extractor=LinkExtractor(restrict_css='#ctl00_c1_volumes_ctl00_chapters')
        i['volumes']=[(link.text,link.url) for link in chaptor_extractor.extract_links(response)]

        return i
