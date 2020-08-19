""" 
    File:channel_category.py
    Author: Eduardo Barrancos
    Description: Functions needed for channel and category management
"""

# Problem: Its possible to have a channel and a category with the same name

async def find_category(guild, category_name):
    """ Returns the category with the name in the guild """
    if not(guild and category_name): return None 

    #Categories' names are always uppercase 
    for category in guild.categories:
        if category.name == category_name.upper(): return category 
    return None


async def find_channel(guild_cat, channel_name):
    """ Returns the channel with the name in the category/guild """
    if not(guild_cat and channel_name): return None

    #Channels' names are always lowercase
    for channel in guild_cat.channels:
        if channel.name == channel_name.lower(): return channel
    return None