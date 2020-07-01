import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

#gh
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!ping'):
        await message.channel.send('Pong!')

#Send a message when a member joins
async def on_member_join(member):
    await member.message(f'Hi, welcome {member.name}!')

client.run('NjkwNTQ0NTcxNzE2NzMwODkx.XvsWYQ.bI_1g6vEmMOg1kQE_xIBJtTP9G8')