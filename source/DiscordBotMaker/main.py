import sys

from PyQt5.QtCore import Qt

import compiler

from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPalette, QColor

import encryption
from ui import Ui_MainWindow


class Dialog(QDialog):
    def __init__(self, title: str, contentLabel: str):
        super().__init__()

        self.cmdtype = ""
        self.cmdname = ""
        self.txtsend = ""

        self.setWindowTitle(title)

        self.layout = QVBoxLayout()

        message = QLabel(contentLabel)
        self.textBox = QLineEdit()
        self.messageBox = QLineEdit()
        self.messageBox.hide()
        typesend = QRadioButton("Send message")
        typesend.toggled.connect(self.typesendoggled)
        typeaddrole = QRadioButton("Add role to user")
        typeaddrole.toggled.connect(self.typeaddroleoggled)
        okbutton = QPushButton("OK")
        okbutton.clicked.connect(self.m_close)

        self.layout.addWidget(message)
        self.layout.addWidget(self.textBox)
        self.layout.addWidget(typesend)
        self.layout.addWidget(self.messageBox)
        self.layout.addWidget(typeaddrole)
        self.layout.addWidget(okbutton)

        self.setLayout(self.layout)

    def typesendoggled(self, clicked):
        if clicked:
            self.cmdtype = "send"
            self.messageBox.show()

    def typeaddroleoggled(self, clicked):
        if clicked:
            self.cmdtype = "addrole"
            self.messageBox.hide()

    def m_close(self):
        self.cmdname = self.textBox.text()
        self.txtsend = self.messageBox.text()
        self.close()


class Window(Ui_MainWindow, QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.setupUi(self)

        self.setupBtn.clicked.connect(self.enterSetup)
        self.commandsBtn.clicked.connect(self.enterCommands)
        self.addCommand.clicked.connect(self.addCommandClicked)
        self.removeCommand.clicked.connect(self.removeItem)
        self.compileBtn.clicked.connect(self.compileBot)

    def enterSetup(self):
        self.stackedWidget.setCurrentIndex(0)
        self.setupBtn.setChecked(True)
        self.commandsBtn.setChecked(False)

    def enterCommands(self):
        self.stackedWidget.setCurrentIndex(1)
        self.setupBtn.setChecked(False)
        self.commandsBtn.setChecked(True)

    def addCommandClicked(self):
        dlg = Dialog("New command", "Please enter command name:")
        dlg.exec()
        if not dlg.cmdname == "":
            self.commandsList.addItem(dlg.cmdname+": "+dlg.txtsend)

    def removeItem(self):
        listItems = self.commandsList.selectedItems()
        if not listItems:
            return
        for item in listItems:
            self.commandsList.takeItem(self.commandsList.row(item))

    def compileBot(self):
        items = []
        print(self.commandsList.count())
        for x in range(self.commandsList.count()):
            items.append(self.commandsList.item(x).text())
        encode = encryption.Encoder(
            ["a", "ą", "b", "c", "ć", "d", "e", "ę", "f", "g", "h", "i", "j", "k", "l", "ł", "m", "n", "o", "ó", "p",
             "r", "s",
             "ś", "t", "u", "v", "w", "x", "y", "z", "ź", "ż", "A", "Ą", "B", "C", "Ć", "D", "E", "Ę", "F", "G", "H",
             "I", "J",
             "K", "L", "Ł", "M", "N", "O", "Ó", "P", "Q", "R", "S", "Ś", "T", "U", "V", "W", "X", "Y", "Z", "Ź", "Ż", "0",
             "1", "2",
             "3", "4", "5", "6", "7", "8", "9", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+",
             "/", "\\",
             ",", ".", "?", "|", ":", ";", "[", "]", "{", "}", "`", "~", " "])
        encodeStr = encode.encode(self.tokenLineEdit.text())
        compiler.compilePyBot(items, self.prefixLineEdit.text(), encodeStr, self.statusLineEdit.text())


def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
