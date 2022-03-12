from pytube import YouTube      # pip install pytube

# Demande du lien à l'utilisateur :
link = input("Entrer Le lien de la vidéo que vous souhaitez télécharger \n=> ")
yt = YouTube(link)

# details
def detail(lien):
    print("Titre: ",lien.title)
    print("Nombre de vus: ",lien.views)
    print("Durée de la vidéo: ",lien.length)
    print("Notation de la vidéo ",lien.rating)
# Meilleur résolution possible
def res(lien):
    res = lien.streams.get_highest_resolution()
    return res

#Starting download
detail(link)
print("Téléchargement en cours...")
res(link).download()
print("Téléchargement terminé!!")