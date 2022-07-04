# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 09:59:15 2022

@author: Muriel
"""
import requests

## function that gets the random quote
def get_random_quote():
    try:
        ## making the get request
        response = requests.get("https://quote-garden.herokuapp.com/api/v3/quotes/random")
        if response.status_code == 200:
            json_data = response.json()
            data = json_data['data']
            
            ##getiong the quote from the data
            print(data[0]['quoteText'])
        else:
            print("Error while getting quote")
    except:
        print("Something went wrong ! Try Again !")

get_random_quote()
            
            
