import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

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