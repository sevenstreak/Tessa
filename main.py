import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from call import * 

load_dotenv()

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))

@bot.command()
async def g(ctx, args):
    await ctx.send(await g(args))
   
@bot.command()
async def descript(ctx, args):
    await ctx.send(await desc(args))

@bot.command()
async def review(ctx, args):
    await ctx.send("Metacritic Score: " + str(await metacritic(args)))

@bot.command()
async def image(ctx, args):
    await ctx.send(await bg(args))


bot.run(os.getenv('TOKEN'))
