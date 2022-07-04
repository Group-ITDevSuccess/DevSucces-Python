# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:41:06 2022

@author: Muriel
"""
import random
random.randint(1, 6)

def lancerUnDe(n):
    d = random.randint(1, n)
    return d

def lancerDeDes(nbDes, nbFaces):
    listeDesDes = []
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)
        listeDesDes.append(d)
    return listeDesDes

def sommeDeDes(nbDes, nbFaces):
    S = 0
    for i in range(nbDes):
        d = lancerUnDe(nbFaces)
        S = S+d
    return S
