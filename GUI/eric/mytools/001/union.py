# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow
import area
import Ui_main.Ui_MainWindow as Ui_MainWindow


class Union(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        super(Ui_MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Pyqt ComboBox')

        self.dictProvince = area.dictProvince
        self.dictCity = area.dictCity
        self.dictTown = area.dicTown

        self.sureBtn.hide()

        self.province.clear()  # 清空items
        self.province.addItem('请选择')
        # 初始化省
        for k, v in self.dictProvince.items():
            self.province.addItem(v, k)  # 键、值反转

    @pyqtSlot(int)
    def on_city_activated(self, index):
        key = self.city.itemData(index)

        self.town.clear()  # 清空items
        if key:
            self.town.addItem('请选择')
            # 初始化县区
            for k, v in self.dictTown[key].items():
                self.town.addItem(v, k)  # 键、值反转

    @pyqtSlot(int)
    def on_province_activated(self, index):
        key = self.province.itemData(index)

        self.town.clear()  # 清空items
        self.city.clear()  # 清空items
        if key:
            # self.lblResult.setText('未选择！')
            self.city.addItem('请选择')
            # 初始化市
            for k, v in self.dictCity[key].items():
                self.city.addItem(v, k)  # 键、值反转

    @pyqtSlot(int)
    def on_town_activated(self, index):
        self.sureBtn.show()

    @pyqtSlot()
    def on_exitButton_clicked(self):
        self.close()

    @pyqtSlot()
    def on_sureBtn_clicked(self):
        province_index = self.province.currentIndex()
        city_index = self.city.currentIndex()
        town_index = self.town.currentIndex()
        # 取当前省市县名称
        province_name = self.province.itemText(province_index)
        city_name = self.city.itemText(city_index)
        town_name = self.town.itemText(town_index)
        # 显示结果
        self.resultedit.setText('{}-{}-{}'.format(province_name, city_name, town_name))

