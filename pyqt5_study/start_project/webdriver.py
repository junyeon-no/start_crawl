from selenium import webdriver
import platform


class WEB_DRVER:
    def __init__(self):
        self.options = webdriver.ChromeOptions() # 옵션 생성
        self.options.add_argument("headless")

        self.windows = 'Windows'
        self.mac = 'Darwin'

        self.ck_os = platform.system()
        if self.ck_os == self.windows :
            self.driver = webdriver.Chrome('C:\python_study\MyPyTest\chromedriver_win32\chromedriver.exe', options = self.options)  # 드라이버 생성    
        elif self.ck_os == self.mac :
            self.driver = webdriver.Chrome('/Users/nojunhyeon/Documents/crawl/start_crawl/pyqt5_study/start_project/chromedriver', options = self.options)
        

    def get_web_driver(self) : 
        return self.driver


if __name__ == "__main__":
    my_WEB_DRVER = WEB_DRVER()
    print(my_WEB_DRVER.ck_os)
    driver = my_WEB_DRVER.get_web_driver()
    driver.get("https://signal.bz/")





    