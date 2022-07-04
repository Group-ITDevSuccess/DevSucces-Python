# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 11:15:17 2022

@author: Muriel
"""

from pytube import YouTube

SAVE_PATH = "D:/YouTube/"

link = "https://www.youtube.com/watch?v=OSDaCh4edAc"

try:
    yt = YouTube(link)
except:
    print("Connection Error !")

mp4files = yt.filter('mp4')

yt.set_filename("Mon Nasheed")

d_video = yt.get(mp4files[-1].extension, mp4files[-1].resolution)

try:
    d_video.downloader(SAVE_PATH)
except:
    print("Somme Error !")

print('Téléchagement Complète')