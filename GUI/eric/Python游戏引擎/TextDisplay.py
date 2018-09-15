# coding=utf-8
import sys, os, threading
import webbrowser, docx, time
from PyQt5 import QtGui, QtCore
from DisplayObject import *
from pylash import *

from eric.Python游戏引擎.pylash import Object, getColor, stage, init


class TextField(DisplayObject):
    '''显示文本用的，还可以用于显示输入框'''
    def __init__(self):
        '''text 显示的文本，是一个str对象
        font 文本字体，也是一个str对象，如：“微软雅黑”
        textColor 文本颜色，str类型，如：“red”
        size 文本尺寸，int类型，默认单位是px
        italic 文本是否是斜体
        weight 文本粗细'''
        super(TextField, self).__init__()

        self.text = ""
        self.font = "Arial"
        self.size = 15
        self.textColor = "#000000"
        self.italic = False
        self.weight = TextFormatWeight.NORMAL

    def _getOriginalWidth(self):
        font = self.__getFont()
        fontMetrics = QtGui.QFontMetrics(font)

        return fontMetrics.width(str(self.text))

    def _getOriginalHeight(self):
        font = self.__getFont()
        fontMetrics = QtGui.QFontMetrics(font)

        return fontMetrics.height()

    def __getFont(self):
        weight = self.weight

        if self.weight == TextFormatWeight.NORMAL:
            weight = QtGui.QFont.Normal
        elif self.weight == TextFormatWeight.BOLD:
            weight = QtGui.QFont.Bold
        elif self.weight == TextFormatWeight.BOLDER:
            weight = QtGui.QFont.Black
        elif self.weight == TextFormatWeight.LIGHTER:
            weight = QtGui.QFont.Light

        font = QtGui.QFont()
        font.setFamily(self.font)
        font.setPixelSize(self.size)
        font.setWeight(weight)
        font.setItalic(self.italic)

        return font

    def _loopDraw(self, c):
        font = self.__getFont()
        flags = QtCore.Qt.AlignCenter
        width = self.width
        height = self.height

        pen = QtGui.QPen()
        pen.setColor(getColor(self.textColor))

        c.setFont(font)
        c.setPen(pen)
        c.drawText(0, 0, width, height, flags, str(self.text))

class TextFormatWeight(Object):
    '''关于字体粗细的常量'''
    NORMAL = "normal"
    BOLD = "bold"
    BOLDER = "bolder"
    LIGHTER = "lighter"

    def __init__(self):
        raise Exception("TextFormatWeight cannot be instantiated.")
if __name__ == '__main__':


    def main():
        txt = TextField()
        # set the content of the text field
        txt.text = "Hello World"
        # set color of text
        txt.textColor = "red"
        # set position
        txt.x = 50
        txt.y = 100
        # set size
        txt.size = 50
        # add text field into display list
        stage.addChild(txt)


    # parameters: refreshing speed, window title, window width, window height, callback
    init(30, "Hello World", 800, 600, main)