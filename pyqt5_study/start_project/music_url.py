import platform
def get_music_url():
    try :
        if platform.system == "Windows" :
            with open("C:\python_study\Job_Craling_Project\pyqt5_study\start_project\music_url.txt", mode="rt", encoding="utf-8") as f :
                get_url = f.readline()
                return get_url
        else :
            with open("music_url.txt", mode="rt", encoding="utf-8") as f :
                get_url = f.readline()
                return get_url
    except FileNotFoundError:
        return ""


def set_music_url(new_url):
    if platform.system == "Windows" :
        with open("C:\python_study\Job_Craling_Project\pyqt5_study\start_project\music_url.txt", mode="wt", encoding="utf-8") as f :
            f.write(new_url)
    else : 
        with open("music_url.txt", mode="wt", encoding="utf-8") as f :
            f.write(new_url)

    

if __name__ == "__main__":
    # set_music_url("test")
    print(get_music_url())