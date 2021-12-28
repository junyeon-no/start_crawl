# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

# KCA return -> [[제목, 날자, 링크],[제목, 날자, 링크]]
def kca_crawlling() :
    BASE_URL = "https://www.kca.kr"
    JOB_URL = "https://www.kca.kr/boardList.do?boardId=CAREERS&pageId=www48"
    KCA_LIST = []
    
    #잘라내기
    result = requests.get(JOB_URL)
    soup = BeautifulSoup(result.text, 'html.parser')
    soup = soup.find("div", {"class": "siiruBoard-list-body"})
    soup_all = soup.find_all("div", {"class": "listBody-row"})

    #제목, 날자, 링크 추출
    for soup_temp in soup_all :
        title = soup_temp.find("a").string
        date = soup_temp.find("p", {"class":"date"}).string
        link = BASE_URL+soup_temp.find("a")["href"]
        list_temp = [title,date,link]
        KCA_LIST.append(list_temp)
    return KCA_LIST # [제목, 날자, 링크]

# KISA return -> [[제목, 날자, 링크],[제목, 날자, 링크]]
def kisa_crawlling() :
    base_url = "https://www.kisa.or.kr"
    url = 'https://www.kisa.or.kr/notice/jobs_List.jsp'
    KISA_LIST = []
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome('C:\python_study\MyPyTest\chromedriver_win32\chromedriver.exe', options = options)  # 드라이버 생성
    action = ActionChains(driver)#액션 체인 생성
    driver.get(url)
    html = driver.page_source  # 웹드라이버 페이지 소스코드 가져오기
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()

    #잘라내기
    soup = soup.find("tbody")
    soup_tr = soup.find_all("tr")   # 공채 단락 때기
    for tr_temp in soup_tr : 
        temp = tr_temp.find_all("td")
        title = temp[1].find("a").getText().strip()  # title
        link = base_url+temp[1].find("a")["href"] # link
        date = temp[2].string  # 날자
        list_temp = [title, date, link] 
        KISA_LIST.append(list_temp)  # [제목, 날자, 링크]
    return KISA_LIST


def algisa_crawlling(type):
    major = "https://cafe.naver.com/ArticleList.nhn?search.clubid=27248370&search.menuid=39&search.boardtype=L"
    public = "https://cafe.naver.com/ArticleList.nhn?search.clubid=27248370&search.menuid=38&search.boardtype=L"
    if type == 'major':
        algisa_url = major
    if type == 'public' :
        algisa_url = public
    base_url = "https://cafe.naver.com/algisa"
    algisa_list = []
    result = requests.get(algisa_url)
    soup = BeautifulSoup(result.text, 'html.parser')
    soup_all = soup.find_all("div", {"class":"article-board m-tcol-c"})
    soup = soup_all[1].find("table")
    div_all = soup.find_all("div",{"class":"board-list"})
    for div in div_all:
        title = div.find("a").string.strip()
        link = base_url + div.find("a")["href"]
        algisa_list.append([title,"생략",link])
    return algisa_list
    
    
if __name__ == '__main__':
    try :
        kca_list = kca_crawlling()
    except :
        print('kca error')
    try :
        kisa_list = kisa_crawlling()
    except :
        print('kisa error')
    try : 
        algisa_public = algisa_crawlling("public")
        algisa_major = algisa_crawlling("major")
    except :
        print("algisa errer")

    print("KCA    ################################################################")
    for kca in kca_list :
        print(kca[0])
        print(kca[1])
        print(kca[2])
        print('---------------------------')
    print("KISA    ################################################################")
    for kisa in kisa_list :
        print(kisa[0])
        print(kisa[1])
        print(kisa[2])
        print('---------------------------')
    
    print("major                            ########################################")
    for algisa in algisa_public :
        for a in algisa:
            print(a)
        print('---------------------------')
    print("public                          ########################################")
    for algisa in algisa_major :
        for a in algisa:
            print(a)
        print('---------------------------')
        
