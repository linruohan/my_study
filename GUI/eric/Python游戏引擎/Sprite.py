#coding=utf-8
from DisplayObject import DisplayObject
from TextDisplay import *
from pylash import *


class Sprite(DisplayObject):
    def __init__(self):
        super(Sprite, self).__init__()

        self.childList = []#显示列表属性
        self.mouseList = []#鼠标事件列表

    def addChild(self, child):
        '''添加对象的方法'''
        self.childList.append(child)

    def removeChild(self, child):
        '''删除对象的方法'''
        self.childList.remove(child)

        child.parent = None

    def _loopDraw(self, c):
        stage._showDisplayList(self.childList)

    def _enterMouseEvent(self, e, cd):
        if not self.visible:
            return

        currentCd = self.__getVisualCoordinate(cd, self)

        isOn = self._isMouseOn(e, currentCd)

        if isOn:
            for o in self.childList[::-1]:
                if (hasattr(o, "_enterMouseEvent") and hasattr(o._enterMouseEvent, "__call__") and o._enterMouseEvent(e,
                                                                                                                      currentCd)):
                    break

            self.__dispatchMouseEvent(e, currentCd)

        return False

    def __getVisualCoordinate(self, origin, obj):
        return {
            "x": origin["x"] + obj.x * origin["scaleX"],
            "y": origin["y"] + obj.y * origin["scaleY"],
            "scaleX": origin["scaleX"] * obj.scaleX,
            "scaleY": origin["scaleY"] * obj.scaleY
        }

    def _isMouseOn(self, e, cd):
        '''鼠标是否盘旋在该Sprite上'''
        if not self.visible:
            return

        childList = self.childList[::-1]

        for o in childList:
            childCd = self.__getVisualCoordinate(cd, o)

            if o._isMouseOn(e, childCd):
                '''设置了target属性，用于方便使用者获取点击对象'''
                e["target"] = o

                return True

        return False

    def __dispatchMouseEvent(self, e, cd):
        '''触发鼠标事件'''
        for o in self.mouseList:
            t = o["eventType"]
            l = o["listener"]

            if t == e["eventType"]:
                eve = object()
                eve.offsetX = e["offsetX"]
                eve.offsetY = e["offsetY"]
                eve.selfX = (e["offsetX"] - cd["x"]) / cd["scaleX"]
                eve.selfY = (e["offsetY"] - cd["y"]) / cd["scaleY"]
                eve.target = e["target"]
                eve.currentTarget = self

                l(eve)

    def addEventListener(self, eventType, listener):
        self.mouseList.append({
            "eventType": eventType,
            "listener": listener
        })

    def removeEventListener(self, eventType, listener):
        for o in self.mouseList:
            if o["eventType"] == eventType and o["listener"] == listener:
                self.mouseList.remove(o)

                break

class MouseEvent(object):
    MOUSE_DOWN = "mouse_down"
    MOUSE_UP = "mouse_up"
    MOUSE_MOVE = "mouse_move"
    MOUSE_OVER = "mouse_over"
    MOUSE_OUT = "mouse_out"
    DOUBLE_CLICK = "mouse_dbclick"

    def __init__(self):
        raise Exception("MouseEvent cannot be instantiated.")
if __name__ == '__main__':
    def main():
        layer = Sprite()
        layer.scaleX = 3
        stage.addChild(layer)

        txt = TextField()
        txt.text = "Test"
        txt.textColor = "red"
        txt.x = 50
        txt.y = 100
        txt.size = 50
        layer.addChild(txt)

        # mouse down event
        layer.addEventListener(MouseEvent.MOUSE_DOWN, onMouseDown)
        # mouse up event
        layer.addEventListener(MouseEvent.MOUSE_UP, onMouseUp)
        # mouse move event
        layer.addEventListener(MouseEvent.MOUSE_MOVE, onMouseMove)


    def onMouseDown(e):
        print("mouse down", e.offsetX, e.offsetY)


    def onMouseUp(e):
        print("mouse up", e.selfX, e.selfY)


    def onMouseMove(e):
        print("mouse move", e.target, e.currentTarget)


    init(30, "Sprite and Mouse Event", 800, 600, main)