#coding=utf-8


import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # self.text = u'\u041b\u0435\u0432 \u041d\u0438\u043a\u043e\u043b\u0430\u0435\u0432\u0438\u0447 \u0422\u043e\u043b\u0441\u0442\u043e\u0439: \n\u0410\u043d\u043d\u0430 \u041a\u0430\u0440\u0435\u043d\u0438\u043d\u0430'
        self.text=u'xiaohan'
        # self.text=u'小寒'
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Font dialog')
        self.show()
    # 绘画事件
    def paintEvent(self,event):
        qp=QPainter()
        qp.begin(self)
        self.drawText(event,qp)
    def drawText(self,event,qp):
        qp.setPen(QColor(168,34,3))
        qp.setFont(QFont('Consolar',20))
        qp.drawText(event.rect(),Qt.AlignCenter,self.text)#西里尔字母.文本垂直和水平对齐
if __name__ == '__main__':
    app=QApplication(sys.argv)
    ex=Example()
    sys.exit(app.exec_())
