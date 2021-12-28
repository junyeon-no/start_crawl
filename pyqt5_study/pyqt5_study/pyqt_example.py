import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit, QPlainTextEdit)
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayosut, QLabel, QLineEdit, QTextEdit)

#pyinstaller -w -F qtextbrowser_advanced.py
# pyinstaller --windowed --onefile qtextbrowser_advanced.py

#QLabel('Label1', self)
#btn1 = QPushButton('Button1', self)

#btn1.move(80, 13)

#####창닫기
#self.close() 창닫기
#quit() 종료

### QPlainTextEdit
## text eidt

#####박스레이아웃
# hbox = QHBoxLayout()
# hbox.addStretch(1)
# hbox.addWidget(okButton)
# hbox.addWidget(cancelButton)
# hbox.addStretch(1)
# vbox = QVBoxLayout()
# vbox.addStretch(3)
# vbox.addLayout(hbox)
# vbox.addStretch(1)
# self.setLayout(vbox)

#####링크
# urlLink="<a href=\"http://www.google.com\">'Click this link to go to Google'</a>" 
# self.L1 = QLabel(urlLink , self)
# self.L1.setOpenExternalLinks(True)


# self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 테이블 스트레치 기준으로 열 맞춤
# self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents) # 테이블 컨텐츠로 열 너비맞춤

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI1()

    def initUI1(self):
        btn = QPushButton("test1", self)
        btn.clicked.connect(self.btn_clicked )
        
        self.resize(300,200)
        self.show()
    

    def initUI2(self):
        grid = QGridLayout()
        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        # self.setGeometry(300, 300, 300, 200)
        self.setLayout(grid)
        self.show()
    
    def btn_clicked(self):
        self.close()
        super().__init__() #새창 띄우기위한 QWidget 초기화
        self.initUI2()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())