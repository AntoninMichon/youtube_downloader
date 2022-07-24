# By HookSander

def pre_quest_test():
    ok = 0
    try :
        import os
    except :
        print("OS module is required for start this program")
        ok += 1
    try :
        import platform
    except :
        print("platform module is required for start this program")
        ok += 1
    try :
        from pytube import YouTube
    except :
        print("Pytube module is required for start this program")
        ok += 1
    if ok != 0 :
        exit()
        


import os
import platform
from pytube import YouTube

device_os = platform.system()   #! => os.startfile work only on windows



def metadata(info):
    """Metadata : give info such as title, numbers of views etc... about the video

    Args:
        info (str): Video youtube link

    Returns:
        bool : if True => Download, else the program quit
    """
    print("Title : {}\nViews : {}\nLength : {} minutes".format(info.title, info.views, info.length/60))
    ask = input("Do you want to download this video ? [Y/n\n=>").lower()
    ok = False
    while not ok :
        if ask == 'y':
            ok = True
            return True
        elif ask == 'n':
            ok = True
            print("Vous avez annulé l'opération.")
            print("You cancelled the operation.")
            return False
        else :
            ask = input("Do you want to download this video ? [Y/n\n=>").lower()

def download(info, title, type_device):
    """Download : start the download of the video in script folder

    Args:
        info (str): video youtube link in it's better quality
        title (str): Title of the video, for open if user want
        type_device (str): give info about the os ('Linux', 'Windows', 'Darwin' => for Mac OS)
    """
    print("Downloading ...")
    info.download()     #! => Start Download
    print("Download done !")
    #? file_path = os.path.realpath(__file__)
    ask = input("Your video is in {}, do you want open it now ? [Y/n]\n=>".format(os.getcwd())).lower()     #! => Display access path
    ok = False
    while not ok :
        if ask =='y':
            ok = True
            if type_device == "Windows" :
                os.startfile(str(title.title)+".mp4")   #! => Open the video un default medi player on client pc
            else :
                print("Sorry, this function is not available for linux and Mac OS, maybe more later")
                exit()
                #TODO vid = str(os.getcwd()+"/"+title.title+".mp4")
                #TODO open (vid)
        elif ask =='n':
            ok = True
            exit()
        else :
            ask = input("Your video is in {}, do you want open it now ? [Y/n]\n=>".format(os.getcwd())).lower()

def main():
    """Start of the program
    """
    link = input("Enter your YouTube video link\n=>")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()     #! For download the better quality available
    if metadata(yt) :
        download(ys, yt, device_os)
    else :
        exit()
        
if __name__ == '__main__' :
    main()