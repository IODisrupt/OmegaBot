import discord
import asyncio
import datetime
import time
import aiohttp
import threading
import glob
import re
import json
import os
import urllib.request
from discord.ext import commands
from random import randint
from random import choice as randchoice
from random import choice as rndchoice
from random import shuffle
from .utils.dataIO import fileIO
from .utils import checks
from bs4 import BeautifulSoup

class Runescape:
    """Runescape-relate commands"""
    
    def __init__(self, bot):
        self.bot = bot
        """
        imLink = http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=
        nmLink = http://services.runescape.com/m=hiscore/index_lite.ws?player=
        """
        
    @commands.command(pass_context=True, no_pm=True)
    async def stats(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            overall = stats[0].split(",")
            await self.bot.say("```" + name + "'s ranking in overall level is: " + overall[0] + "\n" + name + "'s overall level is: " + overall[1] + "\n" + name + "'s total experience is: " + overall[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
    
    #####Overall#####
    @commands.command(pass_context=True, no_pm=True)
    async def overall(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[0].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
    
    #####Attack#####        
    @commands.command(pass_context=True, no_pm=True)
    async def attack(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[1].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Defence#####        
    @commands.command(pass_context=True, no_pm=True)
    async def defence(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[2].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Strength#####        
    @commands.command(pass_context=True, no_pm=True)
    async def strength(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[3].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Constitution#####        
    @commands.command(pass_context=True, no_pm=True)
    async def constitution(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[4].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Ranged#####        
    @commands.command(pass_context=True, no_pm=True)
    async def ranged(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[5].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Prayer#####        
    @commands.command(pass_context=True, no_pm=True)
    async def prayer(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[6].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Magic#####        
    @commands.command(pass_context=True, no_pm=True)
    async def magic(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[7].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

def setup(bot):
    n = Runescape(bot)
    bot.add_cog(n)
