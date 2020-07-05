""" 
    File:channel_category.py
    Author: Eduardo Barrancos
    Description: Functions needed for channel and category management
"""

async def find_category(guild,category_name):
    """ Returns the category with the name in the guild """
    if not(guild and category_name): return None 
        
    for category in guild.categories:
        if category.name == category_name: return category 
    return None


async def find_channel(guild_cat, channel_name):
    """ Returns the channel with the name in the category/guild """
    if not(guild_cat and channel_name): return None

    for channel in guild_cat.channels:
        if channel.name == channel_name: return channel
    return None

# NOT VERY USEFULL IN THE END
# async def create_category(guild, category_name):
#     """ Creates a category and returns it """
#     if not(guild and category_name): return None

#     category = await find_category(guild, category_name)
#     if category: print(f'{category} already exists')
#     else:
#         category = await guild.create_category(category_name)
#         print(f'{category} created')
#     return category


# async def create_channel(guild_category, channel_name, typo='text'):
#     """ Creates a channel and returns it 
#             typo:   'text' -> TextChannel
#                     'voice' -> VoiceChannel"""
#     #Possible type of channels
#     possible_typos = ('text', 'voice')

#     if not(guild_category and channel_name): return None
#     if not (typo in possible_typos): return None

#     channel = await find_channel(guild_category, channel_name)
#     if channel: print(f'{channel} already exists')
#     else:
#         if typo == 'text': channel = await guild_category.create_text_channel(channel_name)
#         elif typo == 'voice': channel = await guild_category.create_voice_channel(channel_name)
#         print(f'{channel} created')
#     return channel
