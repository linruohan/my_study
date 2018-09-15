# -*- coding: utf-8 -*-
from PyQt5.QtCore import pyqtSlot,pyqtSignal,Qt
from PyQt5.QtWidgets import QDialog,QApplication

from Ui_FR_Dialog import Ui_Dialog
import re


class FR_Dialog(QDialog, Ui_Dialog):
    """
    Class documentation goes here.
    """
    nofound = pyqtSignal()
    found = pyqtSignal(int)
    def __init__(self,text,parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(FR_Dialog, self).__init__(parent)
        self.__text = text
        self.__index = 0
        self.setupUi(self)



        MAC = "qt_mac_set_native_menubar" in dir()
        if not MAC:
            self.findButton.setFocusPolicy(Qt.NoFocus)
            self.replaceButton.setFocusPolicy(Qt.NoFocus)
            self.replaceAllButton.setFocusPolicy(Qt.NoFocus)
            self.closeButton.setFocusPolicy(Qt.NoFocus)
        self.updateUi()


    @pyqtSlot(str)
    def on_findLineEdit_textEdited(self, text):
        self.__index = 0
        self.updateUi()


    def makeRegex(self):
        findText = self.findLineEdit.text()
        if self.syntaxComboBox.currentText() == "Literal":
            findText = re.escape(findText)
        flags = re.MULTILINE|re.DOTALL|re.UNICODE
        if not self.caseCheckBox.isChecked():
            flags |= re.IGNORECASE
        if self.wholeCheckBox.isChecked():
            findText = r"\b%s\b" % findText
        return re.compile(findText, flags)


    @pyqtSlot()
    def on_findButton_clicked(self):
        regex = self.makeRegex()
        match = regex.search(self.__text, self.__index)
        if match is not None:
            self.__index = match.end()
            #self.emit(SIGNAL("found"), match.start())
            self.found.emit(match.start())
        else:
            #self.emit(SIGNAL("notfound"))
            self.nofound.emit()


    @pyqtSlot()
    def on_replaceButton_clicked(self):
        regex = self.makeRegex()
        self.__text = regex.sub(self.replaceLineEdit.text(),
                                self.__text, 1)


    @pyqtSlot()
    def on_replaceAllButton_clicked(self):
        regex = self.makeRegex()
        self.__text = regex.sub(self.replaceLineEdit.text(),
                                self.__text)

    def updateUi(self):
        enable = bool(self.findLineEdit.text())
        self.findButton.setEnabled(enable)
        self.replaceButton.setEnabled(enable)
        self.replaceAllButton.setEnabled(enable)



    def text(self):
        return self.__text



if __name__ == "__main__":
    import sys
    text = """US experience shows that, unlike traditional patents,
software patents do not encourage innovation and R&D, quite the
contrary. In particular they hurt small and medium-sized enterprises
and generally newcomers in the market. They will just weaken the market
and increase spending on patents and litigation, at the expense of
technological innovation and research. Especially dangerous are
attempts to abuse the patent system by preventing interoperability as a
means of avoiding competition with technological ability.
--- Extract quoted from Linus Torvalds and Alan Cox's letter
to the President of the European Parliament
http://www.effi.org/patentit/patents_torvalds_cox.html"""

    app = QApplication(sys.argv)
    form = FR_Dialog(text)
    #form.connect(form, SIGNAL("found"), found)
    #form.connect(form, SIGNAL("notfound"), nomore)
    def found(where):
        print("Found at %d" % where)

    def nomore():
        print("No more found")
    form.found.connect(found)
    form.nofound.connect(nomore)
    form.show()
    sys.exit(app.exec_())
    #print form.text()