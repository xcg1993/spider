# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DyttPipeline(object):
    def process_item(self, item, spider):
        print(type(item))
        print('------>',item.get('name'))
    def __del__(self):
        pass
