# HookSander
import os
from pytube import YouTube

def metadata(info):
    print("Title : {}\nViews : {}\nLength : {} secondes".format(info.title, info.views, info.length))
    ask = input("Do you want download this video ? [Y/n]\n=>").lower()
    ok = False
    while not ok :
        if ask == 'y':
            ok = True
            return True
        elif ask == 'n':
            ok = True
            print("You cancel operation.")
            return False
        else :
            ask = input("Do you want download this video ? [Y/n]\n=>").lower()

def download(info, title):
    print("Downloading...")
    info.download()
    print("Download Done !")
    file_path = os.path.realpath(__file__)
    ask = input("Your Video is in {} d you want open it ? [Y/n]\n=>".format(os.getcwd())).lower()
    ok = False
    while not ok :
        if ask =='y':
            ok = True
            os.startfile(str(title.title)+".mp4")
        elif ask =='n':
            ok = True
            exit()
        else :
            ask = input("Your Video is in {} d you want open it ? [Y/n]\n=>".format(os.getcwd())).lower()

def main():
    link = input("Enter your YouTube video link\n=>")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    if metadata(yt) :
        download(ys, yt)
    else :
        exit()
        
main()