import crawling_ck
from crawling_ck import today_ck
from pyqt_ui import *

if(today_ck() == crawling_ck.checked) : 
    app = QApplication(sys.argv)
    ex = Auto_ui()
    sys.exit(app.exec_())

else :
    try :
        app = QApplication(sys.argv)
        ex = Crawl_result_ui()
        sys.exit(app.exec_())
    except :
        print("Crawling ERROR!!!!")

    