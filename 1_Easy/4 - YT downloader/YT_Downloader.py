# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:56:49 2022

@author: Muriel
"""
from tkinter import *
from pytube import YouTube


def download():
    url = YouTube(str(link.get()))
    video = url.streams.last()
    
    #Trier seul MP4
# =============================================================================
#     video = url.streams.filter(progressive=True)
#     video = url.streams.get_highest_resolution()
# =============================================================================
    print("Télechargement ...")
    #Titre de la video
    print("Titre :", url.title)
    #Nombre de vue de la video
    print("Vues :",url.views)
    #Taille de la video
    print("La taille : ", url.length)
    #Description de la video
    print("Description : ", url.description)
    #Rating
    print("Rationg : ",url.rating)
# =============================================================================
#     print(video["video/mp4"])
# =============================================================================
    video.download()
    Label(root, text="Téléchargement Termier", font="arial 15").place(x=140, y=120)


root = Tk()
root.title("Téléchargement de Vidéo Youtube avec Python !")
root.geometry('500x300')
root.resizable(0,0)

Label(root, text="Téléchager gratuitement un vidéo Youtube ",font='San-serif 14 bold').pack()

link= StringVar()

Label(root, text="Coller votre lien ICI :", font='San-serif 15 bold').place(x=150,y=55)

link_enter = Entry(root, width=70, textvariable=link).place(x=30, y = 85)

Button(root, text="Télécharger",font="san-serif 16 bold", bg="lightblue", padx=2,command=download).place(x=180, y=150)


root.mainloop()
