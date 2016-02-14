import discord
from discord.ext import commands
from random import randint
from random import choice as randchoice
import datetime
import time
import aiohttp
import asyncio

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
        if await self.is_admin(msg.author):
            await self.bot.say("Yes, you are!")
        else:
            await self.bot.say("No, you aren't!")
            
            

    async def is_admin(self, author):
        elif author.id == checks.settings["OWNER"]:
            return True
        elif discord.utils.get(author.roles, name=checks.settings["ADMIN_ROLE"]) is not None:
            return True
        elif discord.utils.get(author.roles, name=checks.settings["MOD_ROLE"]) is not None:
            return True
        else:
            return False

def setup(bot):
    n = Runescape(bot)
    bot.add_cog(n)
