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

    #####Cooking#####        
    @commands.command(pass_context=True, no_pm=True)
    async def cooking(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[8].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Woodcutting#####        
    @commands.command(pass_context=True, no_pm=True)
    async def woodcutting(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[9].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Fletching#####        
    @commands.command(pass_context=True, no_pm=True)
    async def fletching(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[10].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Fishing#####        
    @commands.command(pass_context=True, no_pm=True)
    async def fishing(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[11].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Firemaking#####        
    @commands.command(pass_context=True, no_pm=True)
    async def firemaking(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[12].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Crafting#####        
    @commands.command(pass_context=True, no_pm=True)
    async def crafting(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[13].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Smithing#####        
    @commands.command(pass_context=True, no_pm=True)
    async def smithing(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[14].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Mining#####        
    @commands.command(pass_context=True, no_pm=True)
    async def mining(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[15].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Herblore#####        
    @commands.command(pass_context=True, no_pm=True)
    async def herblore(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[16].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
    #####Agility#####        
    @commands.command(pass_context=True, no_pm=True)
    async def agility(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[17].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Thieving#####        
    @commands.command(pass_context=True, no_pm=True)
    async def thieving(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[18].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Slayer#####        
    @commands.command(pass_context=True, no_pm=True)
    async def slayer(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[19].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Farming#####        
    @commands.command(pass_context=True, no_pm=True)
    async def farming(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[20].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Runecrafting#####        
    @commands.command(pass_context=True, no_pm=True)
    async def runecrafting(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[21].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Hunter#####        
    @commands.command(pass_context=True, no_pm=True)
    async def hunter(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[22].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Construction#####        
    @commands.command(pass_context=True, no_pm=True)
    async def construction(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[23].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Summoning#####        
    @commands.command(pass_context=True, no_pm=True)
    async def summoning(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[24].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Dungeoneering#####        
    @commands.command(pass_context=True, no_pm=True)
    async def dungeoneering(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[25].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Divination#####        
    @commands.command(pass_context=True, no_pm=True)
    async def divination(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[26].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

    #####Invention#####        
    @commands.command(pass_context=True, no_pm=True)
    async def invention(self, ctx, name : str):
        address = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name
        
        try:
            website = urllib.request.urlopen(address)
            website_html = website.read().decode(website.headers.get_content_charset())
            stats = website_html.split("\n")
            stat = stats[27].split(",")
            await self.bot.say("```" + name + "'s ranking is: " + stat[0] + "\n" + name + "'s level is: " + stat[1] + "\n" + name + "'s total experience is: " + stat[2] + "```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")

def setup(bot):
    n = Runescape(bot)
    bot.add_cog(n)
