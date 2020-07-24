""" 
    File: bot.py
    Author: Eduardo Barrancos
    Description: Bot that manages a category in your server used for dnd or other games porposes
"""
from channel_category import *

import discord
import asyncio
import json
from discord.ext import commands

# Import TOKEN
import os
os.chdir('../')
with open("Discord_bot.json", "r") as f:
    data = json.load(f)
    TOKEN = data['token']


# The bot instance
bot = commands.Bot(command_prefix='!')

# Name of the channels and categories managed by the bot
anouncChannelName = 'Announcements'
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

        for member in guild.default_role.members:
            if not member.bot:
                #Other bots will have access to channel. Improve
                await anounc.set_permissions(member, read_messages=True, send_messages=False)

        print(f'Finished in {guild}')
        await asyncio.sleep(0.01)



@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return


@bot.command()
async def add(ctx, *nbrs : int):
    """Adds numbers together."""
    sum = 0
    for nbr in nbrs:
        sum += nbr
    await ctx.send(sum)


@bot.command()
async def roll(ctx):
    """  Synopsis:
    !roll xdx [OPTIONS]

    Description:

        xdx : Denotes how many dice to roll and how many sides the dice have.

    The following options are available:

        + - / * : Static modifier

        k# : How many dice to keep out of the roll, keeping highest value.

        r# : Reroll value.

        ir# : Indefinite reroll value.

        t# : Target number for a success.

        f# : Target number for a failure.

        ! : Any text after ! will be a comment.

        Make some functions in other file
 """

@bot.event
async def on_member_join(member):
    await member.message(f'Hi, welcome {member.name}!')

bot.run(TOKEN)

