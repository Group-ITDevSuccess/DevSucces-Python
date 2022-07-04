# -*- coding: utf-8 -*-
"""
Created on Tue Jun 21 13:02:45 2022

@author: Muriel
"""

import discord
from discord.ext import commands
import sys

#-------------------- on récupère le token
with open("token.txt","r",encoding="utf-8") as fichier :
    token= fichier.readline()

#-------------------- on choisit le préfixe pour nos commandes, ici !
bot = commands.Bot(command_prefix="!")

##########################################################################
# à la connexion
##########################################################################
@bot.event
async def on_ready():
    channel = discord.utils.get(bot.get_all_channels(), name="général")  #remplacer "général" par le nom du salon
    await bot.get_channel(channel.id).send("Bonjour à tous !")
    print(f"{bot.user.name} est prêt.")  


##########################################################################
# en cas d'erreur dans les commandes
##########################################################################
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.reply("Vérifier votre commande.")
    else :
        raise error


##########################################################################
# Coucou
##########################################################################
@bot.command(name="coucou")
async def bonjour(ctx):
    reponse=f"Ça va, {ctx.message.author.name} ?"
    await ctx.reply(reponse)
    print(f"Réponse à message {ctx.message.id} : {reponse}")

##########################################################################
# Déconnexion
##########################################################################
@bot.command(name="exit")
async def exit(ctx):
    reponse="Bot déconnecté. Bye Bye !"
    await ctx.reply(reponse)
    await bot.close()
    print(f"Réponse à message {ctx.message.id} : {reponse}")


##########################################################################
##########################################################################
##########################################################################
# Exécution du bot
##########################################################################
##########################################################################
##########################################################################

bot.run(token)