# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:41:30 2022

@author: Muriel
"""

from utils.user_manager import *
from utils.hash_manager import generate_hash, store_key
from utils.encryptor import encrypt_data
from utils.decryptor import decrypt_cipher
from utils.file_manager import encrypt_file, decrypt_file, show_data_file

def menu_1():
	choice = int(input(''' 
		Options
		----------------------------------------------------------------------
		1. New user, REGISTER, GENERATE, STORE master password 
		2. Registered user, LOGIN
		3. Exit
		----------------------------------------------------------------------
		'''))

	if choice == 1 :
		print(f'your choice is : {choice} | ------REGISTER------')
	elif choice == 2 :
		print(f'your choice is : {choice} | ------LOGIN------')
	elif choice == 3 :
		print(f'your choice is : {choice} | ------SEE YA !------')
	else :
		print(f'your choice is : {choice} | ------!!!------')

	return choice

def menu_2():

	choice = int(input(''' 
		Options
		----------------------------------------------------------------------
		1. CRYPT some passwords 
		2. VISUALIZE my data
		3. DECRYPT my password
		4. Exit
		----------------------------------------------------------------------
		'''))	
	
	if choice == 1:
		print(f'your choice is : {choice} | ------CRYPT------')
	elif choice == 2 :
		print(f'your choice is : {choice} | ------VISUALIZE------')
	elif choice == 3 :
		print(f'your choice is : {choice} | ------DECRYPT------')
	elif choice == 4 :
		print(f'your choice is : {choice} | ------SEE YA !------')
	else :
		print(f'your choice is : {choice} | ------!!!------')

	return choice


def main():
	print('')
	print(15*' ',25*'*','PASSWORD MANAGER',27*'*')
	choice_1 = menu_1()
	if choice_1 == 1 :
		username, password = new_user()
		hash = generate_hash(username, password)
		store_key(username, hash)	
	elif choice_1 == 2 :		
		username = input('your name : ')
		password = getpass(prompt='your password : ')		
		if check_user(username, password) :
			choice = menu_2()
			while choice != 4 :
				if choice == 1 :
					encrypt_data(username, password)
					encrypt_file(username, password)
				elif choice == 2 :
					if decrypt_file(username, password):
						show_data_file(username)
					else:
						print('no data stored yet')
					encrypt_file(username, password)
				elif choice == 3 :
					if decrypt_file(username, password) :
						pwd_decrypted = decrypt_cipher(username, password)
						if pwd_decrypted :
							print(pwd_decrypted,'is copied to clipboard ! ')							
						else :
							print('no such service recorded')
						encrypt_file(username, password)
					else:
						print('no data stored yet')
				else:
					exit()
				choice = menu_2()
			exit()
		else:
			exit()

	elif choice_1 == 3 :
		exit()
	else :
		exit()	
	
if __name__ == '__main__':
	main()