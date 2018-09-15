# -*- coding: utf-8 -*-
import os,django
import sys,io
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
from sfspider import spider
from myweb.models import Answer,Question,Tag


class ContentSpider(spider.SegmentfaultQuestionSpider):

    def save(self):
        sf_id=self.url.split('/')[-1]
        tags=[Tag.objects.get_or_create(title=tag_title)[0]for tag_title in self.tags]
        question,created=Question.objects.get_or_create(
            sf_id=sf_id,
            default={'fitle':self.title,'content':self.content}
        )
        question.tags.add(*tags)
        question.save()
        for answer in self.answers:
            Answer.objects.get_or_create(content=answer,question=question)

        return question,created


class TagSpider(spider.SegmentfaultTagSpider):

    def crawl(self): # 采集当前分页
        sf_ids = [url.split('/')[-1] for url in self.questions]
        for sf_id in sf_ids:
            question, created = ContentSpider(sf_id).save()

    def crawl_all_pages(self):
        while True:
            print (u'正在抓取TAG:%s, 分页:%s' % (self.tag_name, self.page)) # 5
            self.crawl()
            if not self.has_next_page:
                break
            else:
                self.next_page()
