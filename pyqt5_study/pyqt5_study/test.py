import sys
from PyQt5.QtWidgets import QApplication, QBoxLayout, QTableWidget, QTableWidgetItem, QWidget, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtWidgets import (QApplication,QTextBrowser, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()

    def MainUI(self):
        self.resize(500,400)

        self.btn = QPushButton("hi", self)
        self.btn.resize(10,3000)
        a = '바로가기'
        link = 'http://www.naver.com'
        label = QLabel("<a href='" + link + "'>" + a + "</a>", self)
        label.setOpenExternalLinks(True)
        # QLabel("<a href=\"http://www.google.com\">'Click this link to go to Google'</a>", self).setOpenExternalLinks(True)

        self.table = QTableWidget()
        self.table.setRowCount(2)
        self.table.setColumnCount(2)
        self.table.setItem(0,0,QTableWidgetItem("네이버"))
        self.table.setItem(1,0,QTableWidgetItem("구글"))
        self.table.setCellWidget(0,1,label)
        self.table.setItem(1,1,QTableWidgetItem("구글----------------------------"))
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents( )
        
        
        self.box = QVBoxLayout()
        
        self.box.addStretch(1)
        self.box.addWidget(self.btn)
        self.box.addStretch(1)
        self.box.addWidget(self.table)
        self.box.addStretch(2)
        self.setLayout(self.box)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())