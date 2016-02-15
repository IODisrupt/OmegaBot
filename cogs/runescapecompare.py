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

class Runescapecompare:
    """Runescape-relate commands"""
    
    def __init__(self, bot):
        self.bot = bot
        """
        imLink = http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=
        nmLink = http://services.runescape.com/m=hiscore/index_lite.ws?player=
        """
        
    @commands.group(name="compare", pass_context=True)
    async def _compare(self, ctx):
        if ctx.invoked_subcommand is None:
            await self.bot.say("Please, choose a skill to compare!")
      
    
    #####Overall#####
    @_compare.command(name="overall", pass_context=True)
    async def compare_overall(self, ctx, name1 : str, name2 : str):
        address1 = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name1
        address2 = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player=" + name2
        
        try:
            website1 = urllib.request.urlopen(address1)
            website2 = urllib.request.urlopen(address2)
            website_html1 = website1.read().decode(website1.headers.get_content_charset())
            website_html2 = website2.read().decode(website2.headers.get_content_charset())
            stats1 = website_html1.split("\n")
            stats2 = website_html2.split("\n")
            stat1 = stats1[0].split(",")
            stat2= stats2[0].split(",")
            if stat1[2] > stat2[2]:
              comparerank = int(stat2[0]) - int(stat1[0])
              comparelvl = int(stat1[1]) - int(stat2[1])
              comparexp = int(stat1[2]) - int(stat2[2])
              await self.bot.say("```" + name1 + "'s ranking is " + str(comparerank) + " ranks higher than " + name2 + "'s rank.\n" + name1 + "'s level is " + str(comparelvl) + " levels higher than " + name2 + "'s.\n" + name1 + "'s total experience is " + str(comparexp) + " higher than " + name2 + "'s.```")
            if stat2[2] > stat1[2]:
              comparerank = stat2[0] - stat1[0]
              comparelvl = stat2[1] - stat1[1]
              comparexp = stat2[2] - stat1[2]
              await self.bot.say("```" + name2 + "'s ranking is " + str(comparerank) + " ranks higher than " + name1 + "'s rank.\n" + name2 + "'s level is " + str(comparelvl) + " levels higher than " + name1 + "'s.\n" + name2 + "'s total experience is " + str(comparexp) + " higher than " + name1 + "'s.```")
        except:
            await self.bot.say("Sorry... Something went wrong there. Did you type the name correctly?")
            
def setup(bot):
    n = Runescapecompare(bot)
    bot.add_cog(n)
