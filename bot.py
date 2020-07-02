""" 
    File: bot.py
    Author: Eduardo Barrancos
    Description: Bot that manages a category in your server used for dnd or other games porposes
"""
from channel_category import *

import discord
import asyncio
from discord.ext import commands

# The bot instance
bot = commands.Bot(command_prefix='!')

# Name of the channels and categories managed by the bot
anouncementChannel = 'Anouncements'
dndcategory = 'DNDTIME'



@bot.event
async def on_ready():
    global dndcategory
    global anouncementChannel

    print(f'We have logged in as {bot.user}')
    print(bot.guilds)

    # Create a category and channels
    # Missing a counter and store the categories and channels in lists or dic  
    for guild in bot.guilds:
        # category
        dndcat = await find_category(guild, dndcategory)
        if not dndcat:
            dndcategory = await guild.create_category(dndcategory)
            print(f'{dndcategory} created')
            anouncementChannel = await dndcategory.create_text_channel(anouncementChannel, position = 0)
            print(f'{anouncementChannel} created')
        else:
            print(f'{dndcategory} already exists in {guild.name}')
            dndcategory = dndcat
            anounc = await find_channel(dndcategory, anouncementChannel)
            if not anounc:
                anouncementChannel = dndcategory.create_text_channel()

        await asyncio.sleep(0.01)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.event
async def on_member_join(member):
    await member.message(f'Hi, welcome {member.name}!')

bot.run('NjkwNTQ0NTcxNzE2NzMwODkx.XvsWYQ.bI_1g6vEmMOg1kQE_xIBJtTP9G8')