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
anouncChannelName = 'Anouncements'
dndCatName = 'DNDTIME'



@bot.event
async def on_ready():
    global dndCatName
    global anouncChannelName

    print(f'We have logged in as {bot.user}')
    print(bot.guilds)

    # Create a category and channels
    for guild in bot.guilds:
        print(f'In {guild}:')
        dndcat = await find_category(guild, dndCatName)
        if not dndcat:
            dndcat = await guild.create_category(dndCatName)
            print(f'{dndcat} created')

            anounc = await dndcat.create_text_channel(anouncChannelName, position=0)
            print(f'{anounc} created')
        else:
            print(f'{dndcat} already exists')
            anounc = await find_channel(dndcat, anouncChannelName)
            if not anounc:
                anounc = await dndcat.create_text_channel(anouncChannelName)
                print(f'{anounc} created')
            else: print(f'{anounc} already exists')

        print(f'Finished in {guild}')
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