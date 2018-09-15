# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#提取内容
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class S123Item(scrapy.Item):
    # define the fields for your item here like:
    # item={}
    name = scrapy.Field()
    title = scrapy.Field()
    info = scrapy.Field()
