# -*- coding: utf-8 -*-

# Define your item pipelines here
#管道
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json

class S123Pipeline(object):
    def __init__(self):
        self.f=open('S123Pipeline.json','wb')
        self.f1=open('S123Pipeline.csv','wb')
        self.f2=open('S123Pipeline.xml','wb')

    def process_item(self, item, spider):
        content=json.dumps(dict(item),ensure_ascii=False)+',\n'
        self.f.write(content.encode('utf-8'))
        self.f1.write(content.encode('utf-8'))
        self.f2.write(content.encode('utf-8'))
        return item

    def close_spider(self,spider):
        self.f.close()
