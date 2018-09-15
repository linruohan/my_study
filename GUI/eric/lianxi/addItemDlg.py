# coding=utf-8
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class FruitDlg(QDialog):
    def __init__(self, title,fruit=None, parent=None):
        super(FruitDlg, self).__init__(parent)
        self.setWindowTitle(title)
        self.fruit=None
        self.resize(300, 100)
        self.setAttribute(Qt.WA_DeleteOnClose)

        grid = QGridLayout(self)
        label = QLabel("fruit name:")
        # 让标签字换行
        label.setWordWrap(True)
        self.fruitlineedit = QLineEdit(fruit)
        validator=QRegExp(r"[^\s][\w\s]+")#正则校验
        self.fruitlineedit.setValidator(QRegExpValidator(validator,self))

        label.setBuddy(self.fruitlineedit)
        self.buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        self.buttonbox.button(QDialogButtonBox.Ok).setDefault(True)
        self.buttonbox.accepted.connect(self.accept)
        self.buttonbox.rejected.connect(self.reject)
        grid.addWidget(label, 0, 0)
        grid.addWidget(self.fruitlineedit, 1, 0)
        grid.addWidget(self.buttonbox, 3, 0)
    def accept(self):
        self.fruit=str(self.fruitlineedit.text())
        QDialog.accept(self)
    def reject(self):
        QDialog.reject(self)

class StringListDlg(QDialog):
    def __init__(self, OriginalList, parent=None):
        super(StringListDlg, self).__init__(parent)
        self.setWindowTitle(" Fruit List")
        self.stringlist = QListWidget()
        if not OriginalList and OriginalList is isinstance(list):
            return
        self.stringlist.addItems(OriginalList)
        self.stringlist.setCurrentRow(0)

        self.add = QPushButton("&add")
        self.edit = QPushButton("&edit")
        self.remove = QPushButton("&remove")
        self.up = QPushButton("&up")
        self.down = QPushButton("&down")
        self.sort = QPushButton("&sort")
        self.close = QPushButton("&close")

        self.add.clicked.connect(self.checkadd)
        self.edit.clicked.connect(self.checkedit)
        self.remove.clicked.connect(self.checkremove)
        self.up.clicked.connect(self.checkup)
        self.down.clicked.connect(self.checkdown)
        self.sort.clicked.connect(self.stringlist.sortItems)
        self.close.clicked.connect(self.closedialog)
        vbox = QVBoxLayout()
        hbox=QHBoxLayout(self)
        vbox.addWidget(self.add)
        vbox.addWidget(self.edit)
        vbox.addWidget(self.remove)
        vbox.addWidget(self.up)
        vbox.addWidget(self.down)
        vbox.addWidget(self.sort)
        vbox.addWidget(self.close)
        hbox.addWidget(self.stringlist)
        hbox.addLayout(vbox)

    def checkadd(self):
        adddlg = FruitDlg("Add Fruit", self)
        if adddlg.exec_():
            self.stringlist.addItem(adddlg.fruit)


    def checkedit(self):
        row=self.stringlist.currentRow()
        fruit=self.stringlist.takeItem(row)
        editdlg = FruitDlg("Edit Fruit",fruit.text(), self)
        if editdlg.exec_():
            self.stringlist.addItem(editdlg.fruit)

    def checkremove(self):
        if QMessageBox.warning(self,u'确认','确定要删除吗？',QMessageBox.Ok|QMessageBox.Cancel):
            itemdelete=self.stringlist.takeItem(self.stringlist.currentRow())
            itemdelete=None


    def checkup(self):
        index=self.stringlist.currentRow()
        if index >0:
            indexnew=index-1
            self.stringlist.insertItem(indexnew,self.stringlist.takeItem(self.stringlist.currentRow()))
            self.stringlist.setCurrentRow(indexnew)

    def checkdown(self):
        index = self.stringlist.currentRow()
        if index < self.stringlist.count():
            indexnew = index+ 1
            self.stringlist.insertItem(indexnew, self.stringlist.takeItem(self.stringlist.currentRow()))
            self.stringlist.setCurrentRow(indexnew)
    def sorted(self):
        self.stringlist.sortItems(Qt.AscendingOrder)
    def closedialog(self):
        QDialog.close(self)
        # self.done()


class Example(QWidget):
    '''standard Dialog'''

    def __init__(self):
        super(Example, self).__init__()
        self.form = None
        self.initUI()
        self.show()

    def initUI(self):
        self.setWindowTitle(u"main edit")
        self.resize(400, 100)
        hlay = QHBoxLayout(self)
        self.myform()

    def myform(self):
        fruit = ["Banana", "Apple", "Fig", "Guava", "Date", "Kiwi", "Plum", "Lemon", ]
        if self.form is None:
            self.form = StringListDlg(fruit, self)
        self.form.show()
        self.form.raise_()  # 激活对话框并使其获得光标
        self.form.activateWindow()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = Example()
    sys.exit(app.exec_())
