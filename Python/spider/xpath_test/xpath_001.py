# -*- coding: utf-8 -*-
import scrapy
class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    # start_urls = ['http://blog.jobbole.com/']
    # http://blog.jobbole.com/112011/
    start_urls = ['http://blog.jobbole.com/112011/']
    def parse(self, response):
        # class="entry-header"
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # [<Selector xpath='//div[@class="entry-header"]/h1/text()' data='可能是迄今为止最好的 GitHub 代码浏览插件'>]
        # extract() 方法可以提取 data 项
        # '//div[@class="entry-header"]/h1/text()'
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace('·','').strip()
        comment_count = response.xpath('//a[contains(@href,"article-comment")]/text()').extract()[0].split(' ')[1]
        fav_count = response.xpath('//i[@class="fa fa-bookmark-o  "]/../text()').extract()[0].split()[0]
        article_content = response.xpath('//div[@class="entry"]').extract()[0]
        category_tag = response.xpath('//a[@rel="category tag"]/text()').extract()[0]
        pass

s=JobboleSpider()
s.parse()
