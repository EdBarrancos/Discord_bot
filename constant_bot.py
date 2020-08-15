""" 
    File: constant_bot.py
    Author: Eduardo Barrancos
    Description: Stores the constants used in bot.py
"""

COMMANDPREFIX = ('!', '$')
# More can be added, using tuples

# Name of the channels and categories managed by the bot
anouncChannelName = "Announcements"
dndCategoryName = "DNDTIME"

########
# Roll #
########
RollName = "roll"
RollAliases = ( "Roll", "ROLL", "rolling", "ROLLING", "Rolling")
RollHelpMessage = """Main command\n
                    Subcommands:
                        !roll dice xdx [OPTIONS]"""
            

RollBriefMessage = """ Inputs random numbers depending on the command provided by the user
            !roll XdX [OPTIONS] """
            
RollDiceSubcommandName = "dice"
RollDiceSubcommandAliases = ("Dice", "DICE")
RollDiceSubcommandHelp = """ dice Subcommand
                            Synopsis:
                            !roll dice xdx [OPTIONS]\n
                            Description:\n
                                xdx : Denotes how many dice to roll and how many sides the dice have.\n
                            The following options are available:\n
                                + - / * : Static modifier\n\n
                                k# : How many dice to keep out of the roll, keeping highest value.\n
                                r# : Reroll value.\n
                                t# : Target number for a success.\n
                                f# : Target number for a failure.\n"""
                                # New option: letter + # or letter(if option doesnt need a number)

########
# Ping #
########

PingName = "ping"
PingAliases = ( "Ping", "PING")
PingHelpMessage = "I'll answer Pong!"
PingBriefMessage = "Type !ping to play Pong!"

#######
# Add #
#######

AddName = "add"
AddAliases = ("Add", "ADD", "sum", "Sum", "SUM")
AddHelpMessage = """Input some numbers and I'll return all of them added together.\n
                    Just remember to leave a blank space between each other"""
AddBriefMessage = "I add numbers together, simple and easy. N N N ..." 

########
# Cool #
########

CoolName = "cool"
CoolAliases = ( "Cool", "COOL")
CoolHelpMessage = "I'll tell you if something is cool"
CoolBriefMessage = "Are you cool? I know I am!"

###########
##### Bot #
###########

BotName = "bot"
BotAliases = ("you", "You")