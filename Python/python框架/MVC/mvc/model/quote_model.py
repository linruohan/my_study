#coding=utf-8

# 只有模型层才能直接访问数据
from lianxi_xuexi.mvc.database.quote import Quotes

class QuotesModel(object):
    '''模型层'''
    def get_quote(self,index):
        '''根据索引读取数据
        @parameter index 索引值'''
        try:
            value=Quotes[index]
        except IndexError as err:
            value="Not Found."
        return  value
