import random
import asyncio
import aiohttp
import time
import discord
from datetime import datetime
from discord.ext import commands

class Error(commands.Cog, name= "Error"):

    def __init__(self,bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_command_error(self ,ctx ,error):
        if isinstance(error,commands.NotOwner):
            em = discord.Embed(title = 'Error While executing command' ,description="You are not the Bot owner" , color = ctx.author.color)

            await ctx.send(embed=em)
        elif isinstance(error,commands.MissingRequiredArgument):
            em = discord.Embed(title = 'Error While executing command' ,description="Wrong usage missing required argument" , color = ctx.author.color)

            await ctx.send(embed=em)
        elif isinstance(error, commands.CommandOnCooldown):
            msg = '**Command on cooldown wait**,{:.2f}s before trying again'.format(error.retry_after)
            await ctx.send(msg)
            await asyncio.sleep(5)
            await ctx.message.delete()
        elif isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send('You Dont Have The required Permissions To run This Command!')
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send("Bot Dont have The reqired Perms uwu")
        else:
            channel = self.bot.get_channel(873104600910143490)
            e = discord.Embed(title = f"Error in : `{ctx.guild.name}`", description = f"Idiot who caused it  : `{ctx.author.name}`",color = 0xff0000)
            e.add_field(name=f"Command name : ",value=f"{ctx.command}")
            e.add_field(name=f"Error name : " ,value=f"{error}")
            e.add_field(name=f"Channel : `{ctx.channel.name}`",value= f"ID : {ctx.channel.id}")
            e.add_field(name=f"Used at : ",value= f"<t:{int(time.time())}:F>")
            e.add_field(name=f"{ctx.message.jump_url}",value="_ _")

            await channel.send(embed = e)

def setup(bot):
    bot.add_cog(Error(bot))
    print("Error cog is loaded")