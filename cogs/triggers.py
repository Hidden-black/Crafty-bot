import discord
from discord.ext import commands

CRAFTY_GUILD_ID = 449227198151262213
TESTING_GUILDS = [846401421317242910, 844487141248598027]

class Triggers(commands.Cog, name= "Triggers"):

    def __init__(self,bot):
        self.bot = bot

        self.craftyPogLog = self.bot.get_guild(CRAFTY_GUILD_ID)
        self.ubl_server = self.bot.get_guild(TESTING_GUILDS[0])

        self.triggers = ["world download"]

        self.crafty_guest_role = self.craftyPogLog.get_role(449229213606739970)
        self.crafty_gamer_role = self.craftyPogLog.get_role(449230130079072257)


    @commands.Cog.listener()
    async def on_message(self, message):
        pass


def setup(bot):
    bot.add_cog(Triggers(bot))
    print("Triggers cog is loaded")
