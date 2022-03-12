from pytube import YouTube      # pip install pytube

# *Demande du lien à l'utilisateur :

link = input("Entrer le lien de la vidéo que vous souhaitez télécharger :\n=>   ")
yt = YouTube(link)

# *Détails :

print("Titre: ",yt.title)
print("Nombre de vu : ",yt.views)
print("Durée de la vidéo: ",yt.length, " secondes")

# *Meilleur résolution:

ys = yt.streams.get_highest_resolution()

# *Début téléchargement :

print("Téléchargement en cours...")
ys.download()
print("Téléchargement terminé !")