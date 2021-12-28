# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

#return [ [제목,링크], [제목, 링크] ]
def security_news_crawlling():
    base_url = 'https://www.boannews.com/'
    crawl_list = []

    # with urllib.request.urlopen(base_url) as response:
    #         html = response.read()
    #         soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')

    webpage = requests.get(base_url, verify=False)
    soup = BeautifulSoup(webpage.content, "html.parser")

    soup_all = soup.find("ul", {"class" : "headline_small_img"}).find_all("li")

    for s in soup_all :
        start = str(s).find("/")
        end = str(s).find(";")
        crawl_list.append([s.string, base_url+str(s)[start:end-1]])
    return crawl_list

#return [ [baseurl] , [keyword, keword] ]
def signal_crawling():
    base_url = 'https://issue.zum.com/daily#!/1'
    crawl_list = []

    # with urllib.request.urlopen(base_url) as response:
    #     html = response.read()
    #     soup = BeautifulSoup(html, 'html.parser', from_encoding='utf-8')
    webpage = requests.get(base_url)
    soup = BeautifulSoup(webpage.content, "html.parser")

    soup_li_all = soup.find("ul" ,{"class":"ranking_list"}).find_all("li")
    
    keyword_list = []
    for li in soup_li_all :
        keyword_list.append(li.find("span", {"class":"word"}).string)   #keyword append
    crawl_list.append([base_url])
    crawl_list.append(keyword_list)
    return crawl_list

#return [ [제목,링크], [제목, 링크] ]
def signal2_crawling():
    base_url = "https://signal.bz/"
    signal_LIST = []
    options = webdriver.ChromeOptions() # 옵션 생성
    options.add_argument("headless")

    driver = webdriver.Chrome('C:\python_study\MyPyTest\chromedriver_win32\chromedriver.exe', options = options)  # 드라이버 생성
    action = ActionChains(driver)#액션 체인 생성
    driver.get(base_url)
    html = driver.page_source  # 웹드라이버 페이지 소스코드 가져오기
    soup = BeautifulSoup(html, 'html.parser')
    driver.quit()
    soup_all = soup.find_all("div", {"class" : "rank-column"})
    for s in soup_all : 
        s_div_all = s.find_all("div")
        for sdiv in s_div_all : 
            link = sdiv.find("a")["href"]
            title = sdiv.find("span", {"class", "rank-text"}).string
            signal_LIST.append([title,link])
    return signal_LIST

if __name__ == "__main__" :
    print(security_news_crawlling())
    # print(signal_crawling())
    # print(signal2_crawling())