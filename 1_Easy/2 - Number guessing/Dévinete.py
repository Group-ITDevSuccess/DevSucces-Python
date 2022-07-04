# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 10:23:16 2022

@author: Muriel
"""
import random

class NumberGuessingGame:
    def __init__(self):
        ##Definir le range
        self.LOWER = 1
        self.HIGHER = 100
    
    #☺Méthode pour générer un random number
    def get_randam_number(self):
        return random.randint(self.LOWER, self.HIGHER)
    
    # Méthode pour démarrer le jeu
    def start(self):
        ##Generer un random number
        random_number = self.get_randam_number()
        print(f" \nEntrer un nombre entre {self.LOWER} à {self.HIGHER}")
        ##La tete du jeu
        chances = 0
        while True:
            user_number = int(input("Entrer le nombre cacher : "))
            if user_number == random_number:
                print(f"-> Gagner ! Vous avez pris entre {chances+1} step{'s' if chances > 1 else ''} !")
                break
            elif user_number < random_number:
                print("-> Votre nombre plus bas !")
            else:
                print("-> Votre nombre plus haute !")
            chances += 1

numberGuessingGame = NumberGuessingGame()
numberGuessingGame.start() 
