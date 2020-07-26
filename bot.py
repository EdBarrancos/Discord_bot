""" 
    File: bot.py
    Author: Eduardo Barrancos
    Description: Bot that manages a category in your server used for dnd or other games porposes
"""
from channel_category import *
from dice import Dice

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

        await anounc.set_permissions(guild.default_role, read_messages=True, send_messages=False)
        print(f'Finished in {guild}')
        await asyncio.sleep(0.01)


@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def add(ctx, *nbrs : int):
    """Adds numbers together."""
    sum = 0
    for nbr in nbrs:
        sum += nbr
    await ctx.send(sum)

@bot.command()
async def roll(ctx, *dice):
    """ Inputs random numbers depending on the command provided by the user"""
    if len(dice) == 0:
        await ctx.send(f'{ctx.author.nick} asked for dice, but gave none.\nIf you need help just type \"!roll help\"')
    elif dice[0] == 'help':
        #Help command
         await ctx.send("""```Synopsis:
        !roll xdx [OPTIONS]\n
        Description:\n
            xdx : Denotes how many dice to roll and how many sides the dice have.\n
        The following options are available:\n
            + - / * : Static modifier\n\n
            k# : How many dice to keep out of the roll, keeping highest value.\n
            r# : Reroll value.\n
            t# : Target number for a success.\n
            f# : Target number for a failure.\n
            ! : Any text after ! will be a comment.```""")
    else:
        await ctx.send(f'{ctx.author.nick} sent the input {dice} with the type {type(dice)}.')
        rolling = Dice()
        await rolling.create(ctx, dice, helpCommand='!roll help')

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

@bot.event
async def on_member_join(member):
    await member.message(f'Hi, welcome {member.name}!')

bot.run(TOKEN)