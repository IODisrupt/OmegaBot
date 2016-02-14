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
        self.ironman = "http://services.runescape.com/m=hiscore_ironman/index_lite.ws?player="
        self.normal = "http://services.runescape.com/m=hiscore/index_lite.ws?player="
    
    @commands.command()
    async def adminstatus(self, ctx):
        """Says if you are an admin or not.
        """
        msg = ctx.message
        
        elif discord.utls.get(author.roles, name=checks.settings["ADMIN_ROLE"]) is not None:
            await self.bot.say("You are an admin.")
        else:
            await self.bot.say("You are nothing!")

def setup(bot):
    n = Runescape(bot)
    bot.add_cog(n)
