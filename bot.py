""" 
    File: bot.py
    Author: Eduardo Barrancos
    Description: Bot that manages a category in your server used for dnd or other games porposes
"""
import discord
import asyncio
import json
from discord.ext import commands

import sys
sys.path.append('./dice')
sys.path.append('./server-management')

from constant_bot import *
from channel_category import find_category, find_channel
from dice import Dice



# Import TOKEN
import os
os.chdir('../')
with open("Discord_bot.json", "r") as f:
    data = json.load(f)
    TOKEN = data['token']


# The bot instance
bot = commands.Bot(COMMANDPREFIX)


###################
## Events #########
###################


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

    for guild in bot.guilds:
        print(f'In {guild}')


@bot.event
async def on_guild_join(guild):
    """ When joinning a guild create channels and categories for the rpg management """

    print(f'In {guild}:')
    dndcat = await find_category(guild, dndCategoryName)
    if not dndcat:
        dndcat = await guild.create_category(dndCategoryName)
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

    await anounc.set_permissions(guild.default_role, read_messages=True, send_messages=False)
    print(f'Finished in {guild}')



@bot.event
async def on_member_join(member):
    await member.message(f'Hi, welcome {member.name}!')

#####################
## Commands #########
#####################

@bot.command()
async def ping(ctx):
    """ Ping? """
    await ctx.send('Pong!')


@bot.command()
async def add(ctx, *nbrs : int):
    """Adds numbers together"""
    sum = 0
    for nbr in nbrs:
        sum += nbr
    await ctx.send(sum)


@bot.command(help=HELPMESSAGE,
            brief=""" Inputs random numbers depending on the command provided by the user
            !roll XdX [OPTIONS]""")
async def roll(ctx, *dice):
    """ Inputs random numbers depending on the command provided by the user
            !roll XdX [OPTIONS]"""
    if len(dice) == 0:
        await ctx.send(f'{ctx.author.nick} asked for dice, but gave none.\nIf you need help just type \"!roll help\"')
    elif dice[0] == 'help':
        #Help command
         await ctx.send(HELPMESSAGE)
    else:
        rolling = Dice()
        await rolling.main(ctx, dice, helpCommand='!help or !help roll')


@bot.group()
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send('No, {0.subcommand_passed} is not cool'.format(ctx))


@cool.command(name='bot')
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')



bot.run(TOKEN)

