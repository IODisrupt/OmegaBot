import random as r
import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
import time
import os

"""deck =[1,2,3,4,5,6,7,8,9,10,10,10,10]*4
player = []
dealer = []
c = 'y'

def __init__(self, bot):
        self.bot = bot
        self.bank = fileIO("data/economy/bank.json", "load")
        self.settings = fileIO("data/economy/settings.json", "load")
        self.payday_register = {}"""

class Blackjack:
"""Blackjack broh"""

        @commands.group(name="blackjack", pass_context=True)
        async def _blackjack(self, ctx):
        """Blackjack Operations"""
                if ctx.invoked_subcommand is None:
                        await self.bot.say("Type !blackjack help")

        @_blackjack.command(pass_context =True)
        async def _help(self, ctx):
        """Blackjack Help"""
                await self.bot.say("Blackjack Help"
                "\n*2"
                "Commands:"
                "\n"
                "!bank register: Registers an account at the Twentysix bank"
                "\n"
                "!bank balance: Shows your current balance"
                "\n")


"""def check_folders():
    if not os.path.exists("data/economy"):
        print("Creating data/economy folder...")
        os.makedirs("data/economy")


def check_files():
    settings ={"PAYDAY_TIME" : 300, "PAYDAY_CREDITS" :120, "BET_MIN" :5, "BET_MAX" :1000}


    f = "data/economy/settings/json"
    if not fileIO(f, "check"):
        print("Creating default economy's settings.json...")
        fileIO(f, "save", settings)


    f = 'data/economy/blank.json'
    if not fileIO(f, "check"):
        print("Creating empty bank.json")
        fileIO(f, "save", {})


 def setup(bot):
        check_folders()
        check_files()"""
