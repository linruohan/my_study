# -*- coding: utf-8 -*-
import scrapy
from s123.items  import S123Item
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class Spider001Spider(scrapy.Spider):
    #爬虫名称
    name = 'spider001'
    #允许爬虫爬取的范围
    # allowed_domains = ['http://www.itcast.cn']
    #启动时开始爬取的url列表
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    #处理
    def parse(self, response):
        # print(response.body)
        node_list=response.xpath("//div[@class='li_txt']")
        #用来存储所有的item字段
        #items=[]
        for node in node_list:
            item=S123Item()
            #.extract()将xpath对象转换为Unicode字符串
            name=node.xpath("./h3/text()").extract()
            title=node.xpath("./h4/text()").extract()
            info=node.xpath("./p/text()").extract()

            item['name']=name[0]
            item['title']=title[0]
            item['info']=info[0]

            # print(name[0])
            # print(title[0])
            # print(info[0])
            #返回每次获取的item值给管道，同时继续执行下面的代码
            yield item
            # return item
            # return scrapy.Request(url)
            # items.append(item)
