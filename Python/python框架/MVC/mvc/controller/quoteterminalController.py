# coding=utf-8

from mvc.model.quote_model import QuotesModel
from mvc.view.quoteteminalview import QuoteTerminalView


class QuoteterminalController(object):
    '''控制器层'''

    def __init__(self):
        self.model = QuotesModel()
        self.view = QuoteTerminalView()

    def run(self):
        n = self.view.select_quote()
        try:
            index = int(n)
            quote = self.model.get_quote(index)
            self.view.show(quote)
        except ValueError as e:
            self.view.error("不合法的索引值")

