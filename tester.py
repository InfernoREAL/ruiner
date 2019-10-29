# -*- coding: utf-8 -*-
# CONFIG
# ---------
token = input("Your Discord Token:")
prefix = "~" #
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



print ("Loading..")


bot = commands.Bot(command_prefix=prefix)
bot.remove_command("help")



bot.run(token)
