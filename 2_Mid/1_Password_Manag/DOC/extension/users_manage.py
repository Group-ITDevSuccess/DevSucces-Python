# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:42:57 2022

@author: Muriel
"""

from os import path
from getpass import getpass
from utils.hash_manager import read_key, valid_password

def new_user():
	username = input('your name : ')
	while path.exists(username+'.key'):
		print('this username is already taken. Choose another one !')
		username = input('your name : ')
	password = getpass(prompt='your master password : ')	
	return username, password

def check_user(username, password):
	if path.exists(username+'.key'):		
		hash = read_key(username)
		if valid_password(hash, password) :
			print(f'user : {username} (correct password, you\'re in)')
			return True
		else :
			print('wrong password')
			return False
	else:
		print('you are not registered yet')
		return False