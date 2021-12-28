a=8
z=3
x = lambda x=a,y=z : x+y
print(x())


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        self.resize(500,400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())