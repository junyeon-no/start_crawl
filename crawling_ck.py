from datetime import datetime
import sqlite3

checked = 1

def today_ck():
    t_d = int(datetime.today().strftime("%y%m%d"))
    job_db_conn = sqlite3.connect("C:\python_study\Job_Craling_Project\Crawling_Db\job_crawling_db.db", isolation_level=None) #db열기
    j_c = job_db_conn.cursor() # db 커서 획득
    j_c.execute("select * from CK order by CK_F DESC")
    ck_temp = j_c.fetchall()[0][0]
    
    # 1 : 크롤링 함 / 0 : 크롤링 안함.
    if ck_temp == t_d : ## 오늘 크롤 했는지 체크
        job_db_conn.close() # db 연결 종료
        return 1
    else :
        j_c.execute("insert into CK values(" + str(t_d) + ")" )
        job_db_conn.close() # db 연결 종료
        return 0

if __name__ == '__main__' :
    if today_ck() == checked : 
        print("크롤링함")
    else : print("크롤링 안함")