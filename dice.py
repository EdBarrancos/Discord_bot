""" 
    File: dice.py
    Author: Eduardo Barrancos
    Description: Manage the dice related funcitons
"""
import asyncio
from constant import * 

class Dice:
    async def create(self, ctx, _input, helpCommand='help'):
        self.guild = ctx
        self.helpCommand = helpCommand

        dice = _input[0]
        dice = dice.split('d')
        print(dice)
        if len(dice) == 1:
            #Input not formated properly
            return await self.somethingWentWrong("Dice information not introduced properly.")
        else:
            i = await self.getDiceInfo(dice)
            if i == self: return self

            self.options = dice[1][i:]
            for i in range(1,len(_input)):
                self.options += _input[i]
        
            self.optionFlags = 0
            # 0000 -> No special options
            # 0001 -> Keep dice out of the roll
            # 0010 -> Reroll values
            # 0100 -> Target number for a success
            # 1000 -> Target number for a failure
            await self.guild.send(f'number of dice: {self.numDice}\n Type of dice: {self.typeDice}\n Options: {self.options}.')
            return self

    async def getOptionsFlags(self):
        """ Return the active flags for this roll """
        return 0

    async def getDiceInfo(self, dice):
        """ Finds the number of dice and the type. 
            Returns the position of the options"""
        if dice[0] == EMPTYSTRING:
            self.numDice = 1
        else:
            try:
                self.numDice = int(dice[0])
            except ValueError:
                return await self.somethingWentWrong("Dice information not introduced properly.")
        
        self.typeDice = EMPTYSTRING
        counter = 0
        size_dice = len(dice[1])
        while counter < size_dice and (dice[1][counter] >= '0' and dice[1][counter] <= '9'):
            self.typeDice += dice[1][counter]
            counter += 1
        
        try:
            self.typeDice = int(self.typeDice)
        except ValueError:
            return await self.somethingWentWrong("Dice information not introduced properly.")
        
        return counter

    async def somethingWentWrong(self, errorMessage):
        """ Sends a error message and inputs the help command """
        await self.guild.send(errorMessage)
        await self.guild.send(f'For more better imformation type {self.helpCommand}.')
        return self
