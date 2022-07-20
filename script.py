# HookSander
import os
import platform
from pytube import YouTube

device_os = platform.system()

def metadata(info):
    print("Titre : {}\nVus : {}\nDurée : {} minutes".format(info.title, info.views, info.length/60))
    ask = input("Voulez-vous télécharher cette vidéo ? [O/n]\n=>").lower()
    ok = False
    while not ok :
        if ask == 'o':
            ok = True
            return True
        elif ask == 'n':
            ok = True
            print("Vous avez annulé l'opération.")
            return False
        else :
            ask = input("Voulez-vous télécharher cette vidéo ? [O/n]\n=>").lower()

def download(info, title, type_device):
    print("Téléchargement en cours ...")
    info.download()
    print("Téléchargement terminé !")
    file_path = os.path.realpath(__file__)
    ask = input("Votre vidéo est dans {} voulez-vous l'ouvrir ? [O/n]\n=>".format(os.getcwd())).lower()
    ok = False
    while not ok :
        if ask =='o':
            ok = True
            if type_device == "Windows" :
                os.startfile(str(title.title)+".mp4")
            else :
                print("Désolé, cette fonctionnalité n'est pas encore disponilbe pour Linux et Mac OS")
                vid = str(os.getcwd()+"/"+title.title+".mp4")
                open (vid)
        elif ask =='n':
            ok = True
            exit()
        else :
            ask = input("Votre vidéo est dans {} voulez-vous l'ouvrir ? [O/n]\n=>".format(os.getcwd())).lower()

def main():
    link = input("Entrer le lien de votre vidéo YouTube\n=>")
    yt = YouTube(link)
    ys = yt.streams.get_highest_resolution()
    if metadata(yt) :
        download(ys, yt)
    else :
        exit()
        
main()