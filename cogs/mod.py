import discord
from discord.ext import commands

class Mod(commands.Cog, name= "Moderation"):

    def __init__(self,bot):
        self.bot = bot




def setup(bot):
    bot.add_cog(Mod(bot))
    print("Moderation cog is loaded")