""" 
    File: constant-bot.py
    Author: Eduardo Barrancos
    Description: Stores the constants used in bot.py
"""

COMMANDPREFIX = '!'
# More can be added, using tuples

# Name of the channels and categories managed by the bot
anouncChannelName = 'Announcements'
dndCategoryName = 'DNDTIME'

HELPMESSAGE = """Synopsis:
        !roll xdx [OPTIONS]\n
        Description:\n
            xdx : Denotes how many dice to roll and how many sides the dice have.\n
        The following options are available:\n
            + - / * : Static modifier\n\n
            k# : How many dice to keep out of the roll, keeping highest value.\n
            r# : Reroll value.\n
            t# : Target number for a success.\n
            f# : Target number for a failure.\n"""
            # New option: letter + # or letter(if option doesnt need a number)