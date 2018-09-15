# -*- coding: utf-8 -*-

"""
Module implementing NewImageDlg.
"""

from PyQt5.QtCore import pyqtSlot, Qt, QVariant
from PyQt5.QtWidgets import QDialog, QApplication, QColorDialog
from PyQt5.QtGui import QPixmap, QBrush, QPainter

from ui_newimagedlg import Ui_NewImageDlg


class NewImageDlg(QDialog, Ui_NewImageDlg):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor
        @param parent reference to the parent widget
        @type QWidget
        """
        super(NewImageDlg, self).__init__(parent)
        self.setupUi(self)
        self.color = Qt.red
        for value, text in (
                (Qt.SolidPattern, "Solid"),
                (Qt.Dense1Pattern, "Dense #1"),
                (Qt.Dense2Pattern, "Dense #2"),
                (Qt.Dense3Pattern, "Dense #3"),
                (Qt.Dense4Pattern, "Dense #4"),
                (Qt.Dense5Pattern, "Dense #5"),
                (Qt.Dense6Pattern, "Dense #6"),
                (Qt.Dense7Pattern, "Dense #7"),
                (Qt.HorPattern, "Horizontal"),
                (Qt.VerPattern, "Vertical"),
                (Qt.CrossPattern, "Cross"),
                (Qt.BDiagPattern, "Backward Diagonal"),
                (Qt.FDiagPattern, "Forward Diagonal"),
                (Qt.DiagCrossPattern, "Diagonal Cross")):
            self.brushComboBox.addItem(text, QVariant(value))

        self.colorButton.clicked.connect(self.getColor)
        self.brushComboBox.activated.connect(self.setColor)
        self.setColor()
        self.widthSpinBox.setFocus()

    def getColor(self):
        color = QColorDialog.getColor(Qt.black, self)
        if color.isValid():
            self.color = color
            self.setColor()

    def setColor(self):
        pixmap = self._makePixmap(60, 30)
        self.colorLabel.setPixmap(pixmap)

    def image(self):
        pixmap = self._makePixmap(self.widthSpinBox.value(),
                                  self.heightSpinBox.value())
        return QPixmap.toImage(pixmap)

    def _makePixmap(self, width, height):
        pixmap = QPixmap(width, height)
        style = self.brushComboBox.itemData(
            self.brushComboBox.currentIndex())
        brush = QBrush(self.color, Qt.BrushStyle(style))
        painter = QPainter(pixmap)
        painter.fillRect(pixmap.rect(), Qt.white)
        painter.fillRect(pixmap.rect(), brush)
        return pixmap