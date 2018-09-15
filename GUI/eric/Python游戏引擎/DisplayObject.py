#coding=utf-8
from pylash import Object
class DisplayObject(Object):
    '''所有显示对象的父类DisplayObject'''

    def __init__(self):
        super(DisplayObject, self).__init__()

        self.parent = None
        # x,y:平面直角坐标系中横纵坐标（原点为屏幕最左上角）
        # rotation表示对象绕其左上角旋转的角度。
        self.x = 0
        self.y = 0
        self.alpha = 1
        self.rotation = 0
        self.scaleX = 1
        self.scaleY = 1
        self.visible = True

    @property
    def width(self):
        '''获取宽'''
        return self._getOriginalWidth() * abs(self.scaleX)

    @property
    def height(self):
        '''获取高'''
        return self._getOriginalHeight() * abs(self.scaleY)

    def _show(self, c):
        if not self.visible:
            return

        c.save()

        c.translate(self.x, self.y)
        c.setOpacity(self.alpha * c.opacity())
        c.rotate(self.rotation)
        c.scale(self.scaleX, self.scaleY)

        self._loopDraw(c)

        c.restore()

    def _loopDraw(self, c):
        '''调用_loopDraw来进行绘制不同的内容'''
        pass

    def _getOriginalWidth(self):
        '''获取宽'''
        return 0

    def _getOriginalHeight(self):
        '''获取height'''
        return 0

    def remove(self):
        '''将自身从显示列表中移除'''
        self.parent.removeChild(self)

    def _isMouseOn(self, e, cd):
        '''判断点击的位置是否在显示对象内'''
        if not self.visible:
            return

        ox = e["offsetX"]
        oy = e["offsetY"]
        x = cd["x"]
        y = cd["y"]
        scaleX = cd["scaleX"]
        scaleY = cd["scaleY"]
        w = self._getOriginalWidth()
        h = self._getOriginalHeight()

        if x <= ox <= x + w * scaleX and y <= oy <= y + h * scaleY:
            e["target"] = self

            return True

        return False