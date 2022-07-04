# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:42:17 2022

@author: Muriel
"""

from argon2 import PasswordHasher
import base64

def generate_hash(username, password):
	hash = PasswordHasher().hash(password)
	print(f'You are registered ! Key for {username} was created successfully.')
	print('Restart the program')
	return hash

def encode_hash(hash):
	encoded_hash = hash.encode()
	encoded_hash = base64.urlsafe_b64encode(encoded_hash[:32])
	return encoded_hash

def store_key(username, key):
	with open(username+'.key','w') as master_pwd:
		master_pwd.write(key)

def read_key(username):
	with open(username+'.key','r') as master_pwd:
		key = master_pwd.read()	
	return key

def valid_password(hash, password):
	try:
		PasswordHasher().verify(hash, password)
		return True
	except:
		return False