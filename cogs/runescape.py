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
import urllib2
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
        imLink = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player="
        nmLink = "http://services.runescape.com/m=hiscore/index_lite.ws?player="
        
    
    @commands.command(pass_context=True, no_pm=True)
    async def imlookup(self, ctx, name : str):
    
    imLink += name   
    
    try:
        website = urllib2.urlopen(imLink)
        website_html = website.read()
        await self.bot.say(website_html)
    except urllib2.HTTPError, e:
        print "Cannot retrieve URL: HTTP Error Code", e.code
    except urllib2.URLError, e:
        print "Cannot retrieve URL: " + e.reason[1]
    
def setup(bot):
    n = Runescape(bot)
    bot.add_cog(n)
