""" 
    File: dice.py
    Author: Eduardo Barrancos
    Description: Manage the dice related funcitons
"""
import random
import asyncio

from .dice_aux.dice import Dice
from .dice_aux.error import Error
from .constant_dice_main import *
from .dice_aux.helful_functions import *
from .quicksort import sortRoll, sortingDirection
from .options.options_impl import *


class Roll:
    async def roll_dice(self, context, _input, helpCommand='help'):
        """ To add an Option:
            Expect a new index in the tuple
            Add a new index and the condicitons for it in the flag
            Add it to help """          
        self.context = context
        self.helpCommand = helpCommand

        dice = Dice()
        dice = await dice.processInputDice(_input)
        if isinstance(dice, Error): 
            return await dice.sendErrorToUser(self.context, self.helpCommand)

        self.roll = await self.rolling(dice)
        self.roll = await sort(self.roll, sortingDirection().biggestToLowest)

        finalStatement = await self.processOptions(dice)

        await self.context.send(f'{self.context.author.mention} rolled:`{self.roll}`. Which means:`{finalStatement}`')      

        if await crited(self.roll, dice):
            await self.crit(self.roll.count(dice.getCeilingNumber()))

        return self
    
    async def processOptions(self, dice):
        
        # 0 -> Keep dice out of the roll
        # 1 -> Reroll values
        # 2 -> Target number for a success
        # 3 -> Target number for a failure
        final = await self.calculateFinal(self.roll)
        
        for optionIndex, optionNumber in enumerate(dice.optionsFlags):
            if optionNumber is not None: 
                if optionIndex == 0:
                    self.roll = processKeepOption(self.roll, optionNumber)
                    final = await self.calculateFinal(self.roll)
                #Fill out the rest
                
        return final
    
    
    async def calculateFinal(self, roll):
        return sum(roll)
    
    
    async def crit(self, totalNumbCrits):
        """ Celebrative message for the Critical hit """
        critTimesStr = await self.getCriticalString(totalNumbCrits)

        msg = await self.context.send(f'F*** YEAH!! {self.context.author.mention} JUST CRITED! {critTimesStr}')
        await self.addReactions(msg, criticalSuccessReactions)

        return self


    async def addReactions(self, msg, reactions: tuple):
        for react in reactions:
            msg.add_reaction(react)
            
        return self
    
    
    async def getCriticalString(self, totalNumbCrits):
        criticalString = f'{totalNumbCrits} times!'
        if totalNumbCrits == 1: criticalString = EMPTYSTRING
        
        return criticalString


    async def rolling(self, dice):
        """ Returns a list with each individual rolls.
                self.numDice elements each from 1 to self.typeDice  """
        
        rolls = list()
        for _ in range(dice.numDice):
            
            rolls.append(await dice.getModifiedNumber(random.randint(STARTROLL, dice.typeDice)))
        
        return rolls
    
    

async def crited(listOfRolls: list, dice) -> bool:
        """ In list_of_roll is there a maximum value? """
        return dice.getCeilingNumber() in listOfRolls  