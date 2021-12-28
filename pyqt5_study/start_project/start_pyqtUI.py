# -*- coding: utf-8 -*-
import sys
import PyQt5
from PyQt5 import QtWidgets
# from PyQt5.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton
# from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)
from PyQt5.QtWidgets import *
from start_crawling import security_news_crawlling,signal_crawling, signal2_crawling
from selenium import webdriver
import pyautogui as pg
from time import sleep
from music_url import set_music_url, get_music_url 
import var

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.MainUI()
        # self.music_url = "https://www.youtube.com/watch?v=XI1BLAV1pO4&list=LL&index=36&t=717s"
    
    def music_start(self): # 뮤직 스타트 셀레늄
        # music url 가져오기
        self.music_url = self.music_edit.text()

        if self.music_url == "" :   ## 가져온 url이 없으면 실행 x
            pass
        else : # url을 성공적으로 가져오면 셀리늄 실행.
            if self.music_url == "s" :
                self.music_url = "https://www.youtube.com/watch?v=7H0XiNHHszk&list=LL&index=4&t=7762s"
            else : 
                set_music_url(self.music_url)
            options = webdriver.ChromeOptions()
            driver = webdriver.Chrome('C:\python_study\MyPyTest\chromedriver_win32\chromedriver.exe', options = options)  # 드라이버 생성
            try : 
                driver.get(self.music_url)
                while(1):
                    click_temp_loc = pg.locateOnScreen("C:\python_study\Job_Craling_Project\pyqt5_study\start_project\youtube.PNG") # 유트브 홈 사진 찾아서 좌표 얻음
                    if(click_temp_loc != None) : 
                        break
                    sleep(1)
                youtube_point = pg.center(click_temp_loc) # 얻은 좌표 중간값 구함.
                pg.click(x = youtube_point.x, y = youtube_point.y + 100 ) # 좌표에서 y축 조금 내려서 클릭

                pg.rightClick()
                pg.moveRel(20, 20)
                pg.click()
                sleep(0.5)
                # pg.keyDown("space")## space를 눌러서 음악 재생
                # pg.keyUp("space")
            except : 
                driver.close()
                QMessageBox.about(self,'Music url error','잘못된 URL입니다.')
        

    def ui_refesh(self):
        self.security_list = security_news_crawlling()
        self.serch_list = signal_crawling() #zum 실시간 사이트 사라짐;;
        self.signal_list = signal2_crawling()
        for i in range(5) :
            self.security_table.setItem(i,0, QTableWidgetItem(self.security_list[i][0]))
            self.urlLink="<a href='" + self.security_list[i][1] + "'>" + self.security_list[i][1] + "</a>" 
            self.L1 = QLabel(self.urlLink , self)
            self.L1.setOpenExternalLinks(True)
            self.security_table.setCellWidget(i,1,self.L1)

        #### signal 실시간 차트 표 채우기      
        for i in range(10) :
            self.signal_table.setItem(i,0, QTableWidgetItem(self.signal_list[i][0]))
            self.urlLink="<a href='" + self.signal_list[i][1] + "'>" + self.signal_list[i][1] + "</a>" 
            self.L1 = QLabel(self.urlLink , self)
            self.L1.setOpenExternalLinks(True)
            self.signal_table.setCellWidget(i,1,self.L1)
        
        ### zum 실시간 차트 표 채우기
        for i in range(10) :
            self.serch_table.setItem(i,0,QTableWidgetItem(self.serch_list[1][i]))


    def MainUI(self):
        self.setWindowTitle("Welcome")
        self.resize(800,800)
        self.show()
        
        self.re_crawl_btn = QPushButton("Refresh", self) # 리프레쉬 버튼 생성
        self.re_crawl_btn.clicked.connect(self.ui_refesh) # 버튼 클릭 -> 리프레쉬

        self.music_edit = QLineEdit() # music url edit
        self.get_url = get_music_url() # 저장된 music.text에서 url 가져온다.
        self.music_edit.setText(self.get_url) # url text에 셋팅한다.

        self.music_btn = QPushButton("Music", self) # 음악 버튼 생성
        self.music_btn.clicked.connect(self.music_start)


        #### table 생성
        vbox = QVBoxLayout() # main layoutbox
        self.security_table = QTableWidget(self)  # 보안 table 생성
        self.security_table.setRowCount(5)# 행 
        self.security_table.setColumnCount(2) # 열
        self.signal_table = QTableWidget(self) # 시그널 table 생성
        self.signal_table.setRowCount(10)# 행
        self.signal_table.setColumnCount(2) # 열
        self.serch_table = QTableWidget(self) # 실시간 검색 table 생성
        self.serch_table.setRowCount(10) # 행
        self.serch_table.setColumnCount(1) # 열

        ### main label 생성
        self.boan_main = QLabel("보안뉴스", self)
        self.signal_main = QLabel("SIGNAL 실시간 차트순위")
        self.serch_main = QLabel("<a href='https://issue.zum.com/daily'>zum실시간 차트순위</a>")
        self.serch_main.setOpenExternalLinks(True)
        self.font1 = self.boan_main.font()
        self.font1.setPointSize(15)
        self.boan_main.setFont(self.font1)
        self.signal_main.setFont(self.font1)
        self.serch_main.setFont(self.font1)
              
        self.ui_refesh()  ### UI - 크롤, 리프레쉬

        #### 테이블 컨텐츠에 맞추어 열 너비 맞추기
        self.security_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.signal_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.serch_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        vbox.addWidget(self.music_edit)
        vbox.addWidget(self.music_btn)
        vbox.addWidget(self.re_crawl_btn)
        vbox.addWidget(self.boan_main)
        vbox.addWidget(self.security_table)
        vbox.addWidget(self.signal_main)
        vbox.addWidget(self.signal_table)
        vbox.addWidget(self.serch_main)
        vbox.addWidget(self.serch_table)
        self.setLayout(vbox)

    


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())

