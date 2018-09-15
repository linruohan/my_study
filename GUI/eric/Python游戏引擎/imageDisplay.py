# coding=utf-8
import sys, os, threading
import webbrowser, docx, time
from PyQt5 import QtGui, QtCore
from DisplayObject import *
from pylash import *
class Loader(DisplayObject):
    '''加载图片'''

    def __init__(self):
        super(Loader, self).__init__()

        self.content = None

    def load(self, url):
        image = QtGui.QImage()
        image.load(url)

        self.content = image


class BitmapData(object):
    '''储存图片'''

    def __init__(self, image=QtGui.QImage(), x=0, y=0, width=0, height=0):
        super(BitmapData, self).__init__()

        self.image = image
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        if image is not None:
            if width == 0:
                self.width = image.width()

            if height == 0:
                self.height = image.height()

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if value > self.image.width():
            value = self.image.width()

        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if value > self.image.height():
            value = self.image.height()

        self.__y = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if (value + self.x) > self.image.width():
            value = self.image.width() - self.x

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if (value + self.y) > self.image.height():
            value = self.image.height() - self.y

        self.__height = value

    def setCoordinate(self, x=0, y=0):
        self.x = x
        self.y = y

    def setProperties(self, x=0, y=0, width=0, height=0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height


class Bitmap(DisplayObject):
    '''显示图片'''

    def __init__(self, bitmapData=BitmapData()):
        super(Bitmap, self).__init__()

        self.bitmapData = bitmapData

    def _getOriginalWidth(self):
        return self.bitmapData.width

    def _getOriginalHeight(self):
        return self.bitmapData.height

    def _loopDraw(self, c):
        '''值得注意的是QPainter的drawImage方法，这个方法接受的参数分别是：[起始点x，起始点y，QImage对象，
        图片显示内容的x属性，图片显示内容的y属性，图片显示内容的宽，
        图片显示内容的高] '''
        bmpd = self.bitmapData

        c.drawImage(0, 0, bmpd.image, bmpd.x, bmpd.y, bmpd.width, bmpd.height)


if __name__ == '__main__':


    def main():
        '''测试'''

        loader = Loader()
        loader.load("./img/001.jpg")

        bmpd = BitmapData(loader.content)
        bmp = Bitmap(bmpd)
        stage.addChild(bmp)
        bmp.x = 80
        bmp.rotation = -10
        bmp.alpha = 0.8
    init(30, "Display An Image", 800, 600, main)


