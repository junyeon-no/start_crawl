import TEST_temp_crawl
import sys
from PyQt5.QtCore import Qt
# from PyQt5.QtWidgets import QApplication, QWidget
# from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from job_crawling import *

class Auto_ui(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Craling') 
        label1 = QLabel('Not crawling because it was crawled', self)
        label1.setAlignment(Qt.AlignCenter)

        # 닫기버튼
        exitButton = QPushButton('exit')
        exitButton.clicked.connect(QCoreApplication.instance().quit)
        # 크롤링 버튼
        crawlingButton = QPushButton('Crawling')
        crawlingButton.clicked.connect(self.crawlingButton_clicked)

        # self.move(300, 300)
        self.resize(250, 100)

        
        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(crawlingButton)
        hbox.addWidget(exitButton)
        hbox.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addWidget(label1)
        vbox.addStretch(2)
        vbox.addLayout(hbox)
        vbox.addStretch(1)
        self.setLayout(vbox)
        self.show()

        
##################################### 왜 되는걸까.. ㅋㅋㅋ
    def crawlingButton_clicked(self) : 
        z = Crawl_result_ui().__init__()
        
        

class Crawl_result_ui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Craling Result') 
        e_Button = QPushButton('exit')
        e_Button.clicked.connect(QCoreApplication.instance().quit)
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(100) # 행 100개
        self.tableWidget.setColumnCount(3) # 열 3개
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        column_headers = ['Title', 'Date', 'Link'] # 열 제목
        self.tableWidget.setHorizontalHeaderLabels(column_headers)# 열 제목 셋팅

        ###############TEST MODE### 수정
        # self.c_dic = {"kisa" : TEST_temp_crawl.kisa, "kca" : TEST_temp_crawl.kca }   # test ------------------ 크롤링 함수로 바꿔주면됨.  +++++ 모듈 추가시 건들어야됨.
        self.c_dic = {"kisa" : kisa_crawlling() , "PUBLIC" : algisa_crawlling("public"), "MAJOR" : algisa_crawlling("major") , "kca" : kca_crawlling()  }
        ###############수정
        self.i =0
        for self.t_key in self.c_dic :
            self.tableWidget.setItem(self.i, 0, QTableWidgetItem(self.t_key))
            self.i = self.i+1
            for self.j in range(10) : # 크롤링 결과 10개만 추출
                for self.z in range(3) :   # 제목, 날자, 링크를 위한 개수 3개
                    ################링크 오픈을 위한 수정중
                    if self.z == 2 :
                        self.urlLink="<a href='" + self.c_dic[self.t_key][self.j][self.z]  + "'>" + self.c_dic[self.t_key][self.j][self.z]  + "</a>"
                        self.L2 = QLabel(self.urlLink , self)
                        self.L2.setOpenExternalLinks(True)
                        self.tableWidget.setCellWidget(self.i, self.z,  self.L2 )
                        
                    else : 
                        self.tableWidget.setItem(self.i, self.z, QTableWidgetItem( self.c_dic[self.t_key][self.j][self.z] ) )
                    ################링크 오픈을 위한 수정중
                    # self.tableWidget.setItem(self.i, self.z, QTableWidgetItem( self.c_dic[self.t_key][self.j][self.z] ) )   # 표에 값 셋팅
                    
                self.i = self.i +1 

        layout = QVBoxLayout()
        layout.addWidget(e_Button)
        layout.addWidget(self.tableWidget) # 생성한 표셋팅
        self.setLayout(layout)
        self.setGeometry(300, 100, 1200, 600)
        self.show()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Crawl_result_ui()
   ex2 = Auto_ui()
   sys.exit(app.exec_())
