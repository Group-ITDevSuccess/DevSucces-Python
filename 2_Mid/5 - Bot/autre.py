# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:03:54 2022

@author: Muriel
"""

##########################################################################
# somme
##########################################################################
@bot.command(name="somme")
async def somme(ctx,val1:int,val2:int):
    reponse=f"{val1} + {val2} = {val1+val2}"
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")