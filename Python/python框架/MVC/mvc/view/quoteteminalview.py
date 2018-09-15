# coding=utf-8

class QuoteTerminalView(object):
    '''视图层'''

    def show(self, quote):
        '''
        显示查询结果
        @parameter quote接收数据
        :param quote:
        :return:
        '''
        print('您查询的名人名言是：%s' % quote)

    def error(self, msg):
        '''打印错误消息
        @msg 接受错误信息
        '''
        print('error:%s' % (msg))

    def select_quote(self):
        '''读取用户的选择'''
        return input('请输入编号进行查询:')
