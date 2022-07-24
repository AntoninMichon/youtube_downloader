# By HookSander

import os
from pytube import YouTube
    
def download_video(link):
    video = YouTube(link)
    videoBestQuality = video.streams.get_highest_resolution()
    print("\nDownloading ...")
    outVideo = videoBestQuality.download()
    print("Done !")
    return outVideo

def download_audio(link) :
    video = YouTube(link)
    extractAudio = video.streams.filter(only_audio=True).first()
    print("\nDownloading...")
    outAudio = extractAudio.download()
    print("Done !")
    return outAudio

def metadata(link) :
    info = YouTube(link)
    print("\nTitle : {}\nViews : {}\nLength : {} minutes".format(info.title, info.views, info.length/60))

def audioOrVideo() :
    userOption = eval(input("\n===Download Option===\n[ 1 ] : Video (.mp4)\n[ 2 ] : Only Audio (.mp3)\n[ 3 ] : exit\n\n=>"))
    ok = False
    while not ok :
        if userOption == 1 :
            ok = True
            return "video"
        if userOption == 2 :
            ok = True
            return "audio"
        if userOption == 3 :
            ok = True
            exit()
        else :
            print("\nWrong input, try again")
            userOption = eval(input("\n===Download Option===\n[ 1 ] : Video (.mp4)\n[ 2 ] : Only Audio (.mp3)\n[ 3 ] : exit\n\n=>"))

def valideDownload(typeFile, title):
    info = YouTube(title)
    if typeFile == 'audio' :
        ask = input("\nDo you want download audio of {} ? [y/n]\n=>".format(info.title)).lower()
        ok = False
        while not ok :
            if ask == 'y' :
                ok = True
                return True
            if ask == 'n' :
                ok = True
                exit()
            else :
                print("\nWrong input, try again")
                ask = input("\nDo you want download audio of {} ? [y/n]\n=>".format(info.title)).lower()
                
    if typeFile == 'video' :
        ask = input("\nDo you want download {} ? [y/n]\n=>".format(info.title))
        ok = False
        while not ok :
            if ask == 'y' :
                ok = True
                return True
            if ask == 'n' :
                ok = True
                exit()
            else :
                print("\nWrong input, try again")
                ask = input("\nDo you want download {} ? [y/n]\n=>".format(info.title))
                

def saveFile(file):
    base, ext = os.path.splitext(file)
    newFile = base + '.mp3'
    os.rename(file, newFile)

def main() :
    link = input("\nEnter your YouTube video link\n=>")
    metadata(link)
    typeFile = audioOrVideo()
    if typeFile == 'video' :
        if valideDownload('video', link) :
            saveFile(download_video(link))
            print("\nVideo is in {}".format(os.getcwd()))
    if typeFile == 'audio' :
        if valideDownload('audio', link) :
            saveFile(download_audio(link))
            print("\nAudio is in {}".format(os.getcwd()))
        
if __name__ == '__main__' :
    main()