#coding=utf-8
#File: Painter Paths Example.py
#Author: Robin
#Date: 2015.2.9
#C++: http://doc.qt.io/qt-5/qtwidgets-painting-painterpaths-example.html
import math
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class RenderArea(QWidget):
    def __init__(self, path, parent=None):
        super(RenderArea, self).__init__(parent)
        self.penWidth = 1
        self.rotationAngle = 0
        self.path = path
        self.setBackgroundRole(QPalette.Base)
        self.setAutoFillBackground(True)
        
    def minimumSizeHint(self):
        return QSize(50, 50)
        
    def sizeHint(self):
        return QSize(100, 100)
        
    def setFillRule(self, rule):
        self.path.setFillRule(rule)
        self.update()
        
    def setFillGradient(self, color1, color2):
        self.fillColor1 = color1
        self.fillColor2 = color2
        self.update()
        
    def setPenWidth(self, width):
        self.penWidth = width
        self.update()
        
    def setPenColor(self, color):
        self.penColor = color
        self.update()
        
    def setRotationAngle(self, degrees):
        self.rotationAngle = degrees
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.scale(self.width() / 100.0, self.height() / 100.0)
        painter.translate(50.0, 50.0)
        painter.rotate(-self.rotationAngle)
        painter.translate(-50.0, -50.0)
        painter.setPen(QPen(self.penColor, self.penWidth, Qt.SolidLine, Qt.RoundCap, Qt.RoundJoin))
        gradient = QLinearGradient(0, 0, 0, 100)
        gradient.setColorAt(0.0, self.fillColor1)
        gradient.setColorAt(1.0, self.fillColor2)
        painter.setBrush(gradient)
        painter.drawPath(self.path)


class MyWindow(QWidget):
    
    def __init__(self):
        super(MyWindow, self).__init__() 
        #self.setUi()
        #self.Pi = 3.1415926
        #矩形路径
        self.rectPath = QPainterPath()
        self.rectPath.moveTo(20.0, 30.0)
        self.rectPath.lineTo(80.0, 30.0)
        self.rectPath.lineTo(80.0, 70.0)
        self.rectPath.lineTo(20.0, 70.0)
        self.rectPath.closeSubpath()
        #圆角矩形路径
        self.roundRectPath = QPainterPath()
        self.roundRectPath.moveTo(80.0, 35.0)
        self.roundRectPath.arcTo(70.0, 30.0, 10.0, 10.0, 0.0, 90.0)
        self.roundRectPath.lineTo(25.0, 30.0)
        self.roundRectPath.arcTo(20.0, 30.0, 10.0, 10.0, 90.0, 90.0)
        self.roundRectPath.lineTo(20.0, 65.0)
        self.roundRectPath.arcTo(20.0, 60.0, 10.0, 10.0, 180.0, 90.0)
        self.roundRectPath.lineTo(75.0, 70.0)
        self.roundRectPath.arcTo(70.0, 60.0, 10.0, 10.0, 270.0, 90.0)
        self.roundRectPath.closeSubpath()
        #椭圆路径
        self.ellipsePath = QPainterPath()
        self.ellipsePath.moveTo(80.0, 50.0)
        self.ellipsePath.arcTo(20.0, 30.0, 60.0, 40.0, 0.0, 360.0)
        #饼图路径
        self.piePath = QPainterPath()
        self.piePath.moveTo(50.0, 50.0)
        self.piePath.arcTo(20.0, 30.0, 60.0, 40.0, 60.0, 240.0)
        self.piePath.closeSubpath()
        #多边形路径
        self.polygonPath = QPainterPath()
        self.polygonPath.moveTo(10.0, 80.0)
        self.polygonPath.lineTo(20.0, 10.0)
        self.polygonPath.lineTo(80.0, 30.0)
        self.polygonPath.lineTo(90.0, 70.0)
        self.polygonPath.closeSubpath()
        #组合路径
        self.groupPath = QPainterPath()
        self.groupPath.moveTo(60.0, 40.0)
        self.groupPath.arcTo(20.0, 20.0, 40.0, 40.0, 0.0, 360.0)
        self.groupPath.moveTo(40.0, 40.0)
        self.groupPath.lineTo(40.0, 80.0)
        self.groupPath.lineTo(80.0, 80.0)
        self.groupPath.lineTo(80.0, 40.0)
        self.groupPath.closeSubpath()
        #文字路径
        self.textPath = QPainterPath()
        self.timesFont = QFont("Consolas", 50)
        self.timesFont.setStyleStrategy(QFont.ForceOutline)
        self.textPath.addText(10, 70, self.timesFont, "寒")
        #贝兹尔路径
        self.bezierPath = QPainterPath()
        self.bezierPath.moveTo(20, 30)
        self.bezierPath.cubicTo(80, 0, 50, 50, 80, 80)
        
        self.starPath = QPainterPath()
        self.starPath.moveTo(90, 50)
        for i in range(5):
            self.starPath.lineTo(50 + 40 * math.cos(0.8 * i * math.pi),
                            50 + 40 * math.sin(0.8 * i * math.pi))
        self.starPath.closeSubpath()
        
        self.renderAreas = []
        self.renderAreas.append(RenderArea(self.rectPath))
        self.renderAreas.append(RenderArea(self.roundRectPath))
        self.renderAreas.append(RenderArea(self.ellipsePath))
        self.renderAreas.append(RenderArea(self.piePath))
        self.renderAreas.append(RenderArea(self.polygonPath))
        self.renderAreas.append(RenderArea(self.groupPath))
        self.renderAreas.append(RenderArea(self.textPath))
        self.renderAreas.append(RenderArea(self.bezierPath))
        self.renderAreas.append(RenderArea(self.starPath))
        
    #def setUi(self):    
        self.fillRuleComboBox = QComboBox()
        self.fillRuleComboBox.addItem("Odd Even", Qt.OddEvenFill)
        self.fillRuleComboBox.addItem("Winding", Qt.WindingFill)

        self.fillRuleLabel = QLabel("Fill &Rule:")
        self.fillRuleLabel.setBuddy(self.fillRuleComboBox)

        self.fillColor1ComboBox = QComboBox()
        self.populateWithColors(self.fillColor1ComboBox)
        self.fillColor1ComboBox.setCurrentIndex(self.fillColor1ComboBox.findText("mediumslateblue"))

        self.fillColor2ComboBox = QComboBox()
        self.populateWithColors(self.fillColor2ComboBox)
        self.fillColor2ComboBox.setCurrentIndex(self.fillColor2ComboBox.findText("cornsilk"))

        self.fillGradientLabel = QLabel("&Fill Gradient:")
        self.fillGradientLabel.setBuddy(self.fillColor1ComboBox)

        self.fillToLabel = QLabel("to")
        self.fillToLabel.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.penWidthSpinBox = QSpinBox()
        self.penWidthSpinBox.setRange(0, 20)

        self.penWidthLabel = QLabel("&Pen Width:")
        self.penWidthLabel.setBuddy(self.penWidthSpinBox)

        self.penColorComboBox = QComboBox()
        self.populateWithColors(self.penColorComboBox)
        self.penColorComboBox.setCurrentIndex(self.penColorComboBox.findText("darkslateblue"))

        self.penColorLabel = QLabel("Pen &Color:")
        self.penColorLabel.setBuddy(self.penColorComboBox)

        self.rotationAngleSpinBox = QSpinBox()
        self.rotationAngleSpinBox.setRange(0, 359)
        self.rotationAngleSpinBox.setWrapping(True)
        self.rotationAngleSpinBox.setSuffix("°")

        self.rotationAngleLabel = QLabel("&Rotation Angle:")
        self.rotationAngleLabel.setBuddy(self.rotationAngleSpinBox)

        self.fillRuleComboBox.activated.connect(self.fillRuleChanged)
        self.fillColor1ComboBox.activated.connect(self.fillGradientChanged)
        self.fillColor2ComboBox.activated.connect(self.fillGradientChanged)
        self.penColorComboBox.activated.connect(self.penColorChanged)

        for it in self.renderAreas: 
            self.penWidthSpinBox.valueChanged.connect(it.setPenWidth)
            self.rotationAngleSpinBox.valueChanged.connect(it.setRotationAngle)

        
        topLayout = QGridLayout()

        i = 0
        for i, it in enumerate(self.renderAreas):
            topLayout.addWidget(it, i // 3, i % 3)
            

        mainLayout = QGridLayout()
        mainLayout.addLayout(topLayout, 0, 0, 1, 4)
        mainLayout.addWidget(self.fillRuleLabel, 1, 0)
        mainLayout.addWidget(self.fillRuleComboBox, 1, 1, 1, 3)
        mainLayout.addWidget(self.fillGradientLabel, 2, 0)
        mainLayout.addWidget(self.fillColor1ComboBox, 2, 1)
        mainLayout.addWidget(self.fillToLabel, 2, 2)
        mainLayout.addWidget(self.fillColor2ComboBox, 2, 3)
        mainLayout.addWidget(self.penWidthLabel, 3, 0)
        mainLayout.addWidget(self.penWidthSpinBox, 3, 1, 1, 3)
        mainLayout.addWidget(self.penColorLabel, 4, 0)
        mainLayout.addWidget(self.penColorComboBox, 4, 1, 1, 3)
        mainLayout.addWidget(self.rotationAngleLabel, 5, 0)
        mainLayout.addWidget(self.rotationAngleSpinBox, 5, 1)
        self.setLayout(mainLayout)

        self.fillRuleChanged()
        self.fillGradientChanged()
        self.penColorChanged()
        self.penWidthSpinBox.setValue(2)

        self.setWindowTitle("Painter Paths")

    def fillRuleChanged(self):
        rule = self.currentItemData(self.fillRuleComboBox)
        for it in self.renderAreas:
            it.setFillRule(rule)

    def fillGradientChanged(self):
        color1 = self.currentItemData(self.fillColor1ComboBox)
        color2 = self.currentItemData(self.fillColor2ComboBox)
        for it in self.renderAreas:
            it.setFillGradient(color1, color2)

    def penColorChanged(self):
        color = self.currentItemData(self.penColorComboBox)
        for it in self.renderAreas:
            it.setPenColor(color)
    
    @staticmethod
    def populateWithColors(comboBox):
        colorNames = QColor.colorNames()
        for name in colorNames:
            comboBox.addItem(name, QColor(name))
    
    @staticmethod
    def currentItemData(comboBox):
        return comboBox.itemData(comboBox.currentIndex(),Qt.UserRole)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())