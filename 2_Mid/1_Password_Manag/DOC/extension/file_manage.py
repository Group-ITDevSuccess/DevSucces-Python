# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:44:45 2022

@author: Muriel
"""

from os import path
from cryptography.fernet import Fernet
from utils import hash_manager
from utils.hash_manager import read_key, encode_hash, valid_password

def read_file(username):
	with open(username+'.credentials','rb') as file :
		lines = file.read()
		return lines

def write_file(username, data):
	with open(username+'.credentials','wb') as file :
		file.write(data)

def encrypt_file(username, password):
	hash = read_key(username)
	if valid_password(hash, password) :
		encoded_hash = encode_hash(hash)
		encryptor = Fernet(encoded_hash)
		
		lines = read_file(username)
		cipher = encryptor.encrypt(lines)

		write_file(username, cipher)

def show_data_file(username):
	with open(username+'.credentials','r') as file :
		lines = file.readlines()
		for line in lines :
			print(line)

def decrypt_file(username, password):
	if path.exists(username+'.credentials'):
		hash = read_key(username)
		if valid_password(hash, password) :
			encoded_hash = encode_hash(hash)
			decryptor = Fernet(encoded_hash)

			lines = read_file(username)
			data = decryptor.decrypt(lines)

			write_file(username, data)
			return True
	else:
		return False