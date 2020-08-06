""" 
    File: dice.py
    Author: Eduardo Barrancos
    Description: Manage the dice related funcitons
"""
import asyncio
import random

from constant_dice import *

class Dice:
    async def main(self, ctx, _input, helpCommand='help'):
        """ To add an Option:
            Expect a new index in the tuple
            Add a new index and the condicitons for it in the flag
            Add it to help """
            
        self.guild = ctx
        self.helpCommand = helpCommand

        dice = _input[0]
        dice = dice.split('d')

        if len(dice) == 1:
            #Input not formated properly
            return await self.somethingWentWrong("Dice information not introduced properly.")
        else:
            i = await self.getDiceInfo(dice)
            if i == self: return self

            self.options = dice[1][i:]
            for i in range(1,len(_input)):
                self.options += _input[i]
        
            optionFlags = await self.getOptionsFlags()
            if optionFlags == self: return self
            # 0 -> Keep dice out of the roll
            # 1 -> Reroll values
            # 2 -> Target number for a success
            # 3 -> Target number for a failure

            roll = await self.rolling()
            await self.guild.send(f'{self.guild.author.mention} rolled:{roll}')
            return self
    
    async def rolling(self):
        """ Returns a list with each individual rolls.
                self.numDice elements each from 1 to self.typeDice  """

        rolls = list()
        for _ in range(self.numDice):
            rolls.append(random.randint(STARTROLL, self.typeDice))
        return rolls


    async def getOptionsFlags(self):
        """ Return the options for this roll and checks for modifiers """

        flag = list()
        for _ in range(NumberOfOptions):
            flag.append(EMPTYSTRING)

        extractingOp = 0
        # 0 -> No op
        # 1 -> Found a op
        # 2 -> Found at least a number
        extractingMod = 0
        # 0 -> No mod
        # 1 -> Found a mod
        # 2 -> Found at least a number
        self.modifier = EMPTYSTRING

        for i in self.options:
            if extractingOp == 2:
                #Last State
                if isNumber(i):
                    flag[index] += i
                else:
                    extractingOp = 0

            elif extractingMod == 2:
                #Last State
                if isNumber(i):
                    self.modifier += i
                else:
                    extractingMod = 0

            if extractingOp == 0 and extractingMod == 0:
                # Idle State
                # Searching
                if i in Operators:
                    self.modifier += i
                    extractingMod = 1
                elif i in OptionsWNumber:
                    index = OptionsWNumber.index(i)
                    extractingOp = 1
                elif i in Options:
                    index = len(OptionsWNumber) + Options.index(i)
                    flag[index] = ACTIVE
                    extractingOp = 2

            elif extractingOp == 1:
                # Transition State
                if isNumber(i):
                    if flag[index] == None: flag[index] = i
                    else: flag[index] += i
                    extractingOp = 2
                else: return await self.somethingWentWrong("Options wrongly formated") 

            elif extractingMod == 1:
                # Transition State
                if isNumber(i):
                    self.modifier += i
                    extractingMod = 2
                else: return await self.somethingWentWrong("Options wrongly formated")
        
        if extractingOp == 1 or extractingMod == 1: return await self.somethingWentWrong("Options wrongly formated")
        return flag

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
        while counter < size_dice and (isNumber(dice[1][counter])):
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

def isNumber(st):
    return st >= "0" and st <= "9"
