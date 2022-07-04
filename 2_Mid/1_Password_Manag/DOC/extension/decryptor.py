# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:44:22 2022

@author: Muriel
"""

from cryptography.fernet import Fernet
from utils.hash_manager import read_key, encode_hash, valid_password
import pyperclip as pc

def get_cipher(username, service_name) :
	with open(username+'.credentials','r') as credentials :
		line = credentials.readline()
		while line :
			data = line.split('\t')
			if data[0] == service_name:
				return data[2]
			line = credentials.readline()
		return False

def decrypt_cipher(username, password):	
	hash = read_key(username)
	if valid_password(hash, password) :
		service_name = input('service_name : ')
		pwd_encrypted = get_cipher(username, service_name)

		encoded_hash = encode_hash(hash)
		decryptor = Fernet(encoded_hash)

		if pwd_encrypted :
			pwd_encrypted = pwd_encrypted.encode()
			pwd_decrypted = decryptor.decrypt(pwd_encrypted)
			pwd_decrypted = pwd_decrypted.decode()
			pc.copy(pwd_decrypted)
			return pwd_decrypted
		else :
			return False