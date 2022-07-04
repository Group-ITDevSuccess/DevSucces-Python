# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 18:54:50 2022

@author: Muriel
"""
from utils.gestion_utilisateur import *
from utils.gestion_hash import generate_hash, store_key
from utils.encrypteur import encrypt_data
from utils.decrypteur import decrypt_cipher
from utils.gestion_fichier import encrypt_file, decrypt_file, show_data_file

def menu_1():
    choice = int(input('''
            Options
            ----------------------------------------------------------------------
            1. Nouvelle Utilisateur? ENREGISTRER, GENERER, ACHETER master password
            2. Enregistrer Utlisateur, LOGIN
            3. Sortir
            ----------------------------------------------------------------------
            '''))

    if choice == 1:
        print(f'Votre choix est : {choise} | -----ENREGISTREMENT-----')
    elif choice == 2:
        print(f'Votre choix est : {choise} | -----LOGIN-----')    
    elif choice == 3:
        print(f'Votre choix est : {choise} | -----AU REVOIR-----')
    else:
        print(f'Votre choix est : {choice} |------!!!------')
        
    return choice

def menu_2():
    choice = int(input('''
        Options
        --------------------------------------------------------------------------
        1. CRYPTER quelque mot de passe
        2. VISUALISER my donnée
        3. DECRYPTER mon mot de pass
        4. Sortir
        --------------------------------------------------------------------------                      
        '''))
  
    if choice == 1 :
        print(f'Votre choix est : {choise} | -----CRYPTER-----')
    elif choice == 2 :
        print(f'Votre choix est : {choise} | -----VISUALISER-----')
    elif choice == 3 :
        print(f'Votre choix est : {choise} | -----DECRYPTER-----')    
    elif choice == 4 :
        print(f'Votre choix est : {choise} | -----AU REVOIR-----')
    else:
        print(f'Votre choix est : {choice} |------!!!------')
    
    return choice

def main():
    print('')
    print(15*' ',25*'*','GESTION DE MOT DE PASSE',20*'*')
    choice_1 = menu_1()
    if choice_1 == 1 :
        username, password = new_user()
        hash = generate_hash(username, password)
        store_key(username, hash)
    elif choice_1 == 2:
        username = input("Votre nom : ")
        password = getpass(prompt='Votre Mot de Passe : ')
        if check_user(username, password):
            choice = menu_2()
            while choice !=4:
                
                if choice == 1 :
                    encrypt_data(username, password)
                    encrypt_file(username, password)
                    
                elif choice == 2:
                    if decrypt_file(username, password):
                        show_data_file(username)
                    else:
                        print('Aucun donnée enregister encore !')
                    encrypt_file(username, password)
                    
                elif choice == 3:
                    if decrypt_file(username, password):
                        pwd_decrypted = decrypt_cipher(username, password)
                        if pwd_decrypted:
                            print(pwd_decrypted, ' etait copier au clipboard !')
                        else:
                            print('Aucun service enregister !')
                        encrypt_file(username, password)
                    else:
                        print("PAS encore d'enregistrement !")
                else:
                    exit()
                choice = menu_2()
            exit()
        else:
            exit()
    
    elif choice_1 == 3:
        exit()
    else:
        exit()
        
if __name__ == '__main__':
    main()
                

    
        
