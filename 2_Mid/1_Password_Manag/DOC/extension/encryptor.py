# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 12:44:00 2022

@author: Muriel
"""
from os import path
from cryptography.fernet import Fernet
from getpass import getpass
from utils.hash_manager import read_key, encode_hash, valid_password
from utils.file_manager import decrypt_file

def encrypt_data(username, password):
	hash = read_key(username)
	if valid_password(hash, password) :
		service_name = input('service name : ')
		username_service = input(f'your username for {service_name} : ')
		pwd_service = getpass(prompt=f'your password for {service_name} : ')
		
		encoded_hash = encode_hash(hash)
		encryptor = Fernet(encoded_hash)
		cipher = encryptor.encrypt(pwd_service.encode())
		store_credentials(username, password, service_name, username_service, cipher)

def store_credentials(username, password, service_name, username_service, cipher):
	if path.exists(username+'.credentials'):
		decrypt_file(username, password)
	with open(username+'.credentials','a') as credentials :
		credentials.write(service_name+'\t'+username_service+'\t'+cipher.decode()+'\n')
		print("your data has been stored successfully")
