import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QPushButton, QLineEdit
from PyQt5.QtGui import QIcon
from PyQt5 import uic

class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_gui()
        self.str_ = ""

    def init_gui(self):
        uic.loadUi('untitled2.ui', self)

        self.pushButton.clicked.connect(lambda state, something='9' : self.button_write(something))
        self.pushButton_2.clicked.connect(lambda state, something='8' : self.button_write(something))
        self.pushButton_3.clicked.connect(lambda state, something='7' : self.button_write(something))
        self.pushButton_4.clicked.connect(lambda state, something='6' : self.button_write(something))
        self.pushButton_5.clicked.connect(lambda state, something='5' : self.button_write(something))
        self.pushButton_6.clicked.connect(lambda state, something='4' : self.button_write(something))
        self.pushButton_7.clicked.connect(lambda state, something='3' : self.button_write(something))
        self.pushButton_8.clicked.connect(lambda state, something='2' : self.button_write(something))
        self.pushButton_9.clicked.connect(lambda state, something='1' : self.button_write(something))
        self.pushButton_15.clicked.connect(lambda state, something='0': self.button_write(something))
        self.pushButton_14.clicked.connect(self.but_equal)
        self.pushButton_10.clicked.connect(lambda state, something='+': self.button_write(something))
        self.pushButton_12.clicked.connect(lambda state, something='-': self.button_write(something))
        self.pushButton_13.clicked.connect(lambda state, something='*': self.button_write(something))
        self.pushButton_11.clicked.connect(lambda state, something='/': self.button_write(something))
        self.pushButton_16.clicked.connect(self.clear)
        self.show()

    def button_write(self, something):
        self.textEdit.clear()
        self.str_ += str(something)
        self.textEdit.setText(self.str_)

    def but_equal(self):
        print(eval(self.str_))
        self.textEdit.setText(str(eval(self.str_)))

    def clear(self):
        self.textEdit.clear()
        self.str_ = ""


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())
