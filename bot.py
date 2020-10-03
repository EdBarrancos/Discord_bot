import discord
import asyncio
from decouple import config
from discord.ext import commands

from constant_bot import *
from server_management.channel_category import find_category, find_channel
from dice.dice_main import Roll



# Import TOKEN
TOKEN = config('TOKEN')


# The bot instance
bot = commands.Bot(COMMANDPREFIX)


###################
## Events #########
###################


@bot.event
async def on_ready():
    """ Triggers when the bot is done preparing the data received from Discord """
    print(f'We have logged in as {bot.user}')

    for guild in bot.guilds:
        print(f'In {guild}')


@bot.event
async def on_guild_join(guild):
    """ Triggers when joining a guild. Creates the category and channels managed by the bot """

    print(f'Just entered {guild}.')
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
    """ Triggers when a new member joins the guild """
    # Not tested
    await member.message(f'Hi, welcome {member.name}!')

#####################
## Commands #########
#####################

@bot.command(name=PingName,
            aliases=PingAliases,
            help=PingHelpMessage,
            brief=PingBriefMessage)
async def ping(ctx):
    """ Ping? """
    await ctx.send('Pong!')



@bot.command(name=AddName,
            aliases=AddAliases,
            help=AddHelpMessage,
            brief=AddBriefMessage)
async def add(ctx, *nbrs : int):
    """Adds numbers together"""
    sum = 0
    for nbr in nbrs:
        sum += nbr
    await ctx.send(sum)



@bot.group(name=RollName,
            aliases=RollAliases,
            help=RollHelpMessage,
            brief=RollBriefMessage)
async def roll(ctx, *args):
    """ Main Command
        Subcommands: 
            XdX [OPTIONS] """
    if len(args) == 0:
        await ctx.send(f'{ctx.author.mention} asked for dice, but gave none.\nIf you need help just type \"!help roll\"')
    else:
        await _rollDice(ctx, args)
        
   

async def _rollDice(ctx, dice):
    """ Inputs random numbers depending on the command provided by the user
            !roll dice XdX [OPTIONS] """
    rolling = Roll()
    await rolling.roll_dice(ctx, dice, helpCommand='!help or !help roll')

    
    
@bot.group(name=CoolName,
           aliases=CoolAliases,
           help=CoolHelpMessage,
           brief=CoolBriefMessage)
async def cool(ctx):
    """Says if a somthing is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} is not cool')


@cool.command(name=BotName,
              aliases=BotAliases)
async def _bot(ctx):
    """Is the bot cool?"""
    await ctx.send('Yes, the bot is cool.')
    
    
@cool.command(name=BrunoName,
              aliases=BrunoAliases)
async def _bruno(ctx):
    """ Is Bruno cool?  """
    await ctx.send('Of course!')


bot.run(TOKEN)

