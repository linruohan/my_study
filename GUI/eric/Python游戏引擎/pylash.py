#coding=utf-8
import sys,os,threading
from PyQt5.QtWidgets import *
import webbrowser,docx,time
from PyQt5 import QtGui, QtCore


class Object(object):
    latestObjectIndex = 0

    def __init__(self):
        Object.latestObjectIndex += 1
        self.objectIndex = Object.latestObjectIndex


class CanvasWidget(QWidget):
    def __init__(self):
        super(CanvasWidget, self).__init__()

        self.setMouseTracking(True)#用于不停地触发移动事件，否则Qt默认只处理一次

    def paintEvent(self, event):
        stage._onShow()

    def mousePressEvent(self, event):
        self.__enterMouseEvent(event, "mouse_down")

    def mouseMoveEvent(self, event):
        self.__enterMouseEvent(event, "mouse_move")

    def mouseReleaseEvent(self, event):
        self.__enterMouseEvent(event, "mouse_up")

    def __enterMouseEvent(self, event, eventType):
        '''offsetX，offsetY：鼠标相对于屏幕左上角的位置
            eventType：鼠标事件类型
            target：鼠标所点击的显示对象，初始值为None，当事件传递到需要获取此属性的时候，就会被赋值为被点击的对象'''
        e = {"offsetX" : event.x(), "offsetY" : event.y(), "eventType" : eventType, "target" : None}

        stage._enterMouseEvent(e, {"x" : 0, "y" : 0, "scaleX" : 1, "scaleY" : 1})


class Stage(Object):
    def __init__(self):
        super(Stage, self).__init__()

        self.parent = "root"
        self.width = 0
        self.height = 0
        self.speed = 0
        self.app = None
        self.canvasWidget = None
        self.canvas = None
        self.timer = None
        self.childList = []
        self.backgroundColor = None

    def _setCanvas(self, speed, title, width, height):
        self.speed = speed
        self.width = width
        self.height = height

        self.canvas = QtGui.QPainter()

        self.canvasWidget = CanvasWidget()
        self.canvasWidget.setWindowTitle(title)
        self.canvasWidget.setFixedSize(width, height)
        self.canvasWidget.show()

        self.timer = QtCore.QTimer()
        self.timer.setInterval(speed)
        self.timer.start();
        self.timer.timeout.connect(self.canvasWidget.update)
        # QtCore.QObject.connect(self.timer, QtCore.SIGNAL("timeout()"), self.canvasWidget, QtCore.SLOT("update()"))

    def _onShow(self):
        self.canvas.begin(self.canvasWidget)

        if self.backgroundColor is not None:
            self.canvas.fillRect(0, 0, self.width, self.height, getColor(self.backgroundColor))
        else:
            self.canvas.eraseRect(0, 0, self.width, self.height)

        self._showDisplayList(self.childList)

        self.canvas.end()

    def _showDisplayList(self, childList):
        for o in childList:
            if hasattr(o, "_show") and hasattr(o._show, "__call__"):
                o._show(self.canvas)

    def addChild(self, child):
        if child is not None:
            child.parent = self

            self.childList.append(child)
        else:
            raise ValueError("parameter 'child' must be a display object.")

    def removeChild(self, child):
        if child is not None:
            self.childList.remove(child)

            child.parent = None
        else:
            raise ValueError("parameter 'child' must be a display object.")



stage = Stage()
def init(speed, title, width, height, callback):

    stage.app =QApplication(sys.argv)

    stage._setCanvas(speed, title, width, height)

    if not hasattr(callback, "__call__"):
        raise ValueError("parameter 'callback' must be a function.")

    callback()

    stage.app.exec_()

def getColor(color):
    if isinstance(color, QtGui.QColor):
        return color
    elif not color:
        return QtCore.Qt.transparent
    else:
        colorObj = QtGui.QColor()
        colorObj.setNamedColor(color)

        return colorObj