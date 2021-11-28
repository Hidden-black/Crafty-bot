import discord
from discord.ext import commands

class Triggers(commands.Cog, name= "Triggers"):

    def __init__(self,bot):
        self.bot = bot
        self.triggers = ["world download"]


    @commands.Cog.listener()
    async def on_message(self, message):
        pass


def setup(bot):
    bot.add_cog(Triggers(bot))
    print("Triggers cog is loaded")
