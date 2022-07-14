# HookSander
import os
from pytube import YouTube

def metadata(info):
    print("Title : {}\nViews : {}\nLength : {} secondes".format(info.title, info.views, info.length))
    ask = input("Do you want download this video ? [Y/n]\n=>").lower()
    if ask == 'y':
        return True
    else :
        print("You cancel operation.")
        return False

def download(info, title):
    print("Downloading...")
    info.download()
    print("Download Done !")
    file_path = os.path.realpath(__file__)
    ask = input("Your Video is in {} d you want open it ? [Y/n]\n=>".format(os.getcwd())).lower()
    if ask =='y':
        os.startfile(str(title.title)+".mp4")
    else :
        exit()

def main():
    link = input("Enter your YouTube video link\n=>")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    if metadata(yt) :
        download(ys, yt)
    else :
        exit()
        
main()