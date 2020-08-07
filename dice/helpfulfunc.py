""" 
    File: helpfulfunc.py
    Author: Eduardo Barrancos
    Description: Helpful functions to manage abstraction
"""

async def isNumber(st: str) -> bool:
    """ Checks if a string is a number string """
    return st >= "0" and st <= "9"

async def crited(listOfRolls: list, typeDice: str, modifier: str) -> bool:
        """ In list_of_roll is there a maximum value? """
        return eval(f'{typeDice}{modifier}') in listOfRolls