import discord
from discord.ext import commands

class Games(commands.Cog, name= "Games"):

    def __init__(self,bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Games(bot))
    print("Games cog is loaded")