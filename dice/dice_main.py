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
from .quicksort import sort, sortingDirection
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
        self.roll = await sort(self.roll, sortingDirection.biggestToLowest)

        finalStatement = await self.processOptionsReturnFinalStatement(dice)

        await self.context.send(f'{self.context.author.mention} rolled:`{self.roll}`. Which means:`{finalStatement}`')      

        if await critedSuccess(self.roll, dice):
            await self.crit(self.roll.count(await dice.getCeilingNumber()), criticalSuccessMessage, criticalSuccessReactions)
            
        if await critedFailure(self.roll, dice):
            await self.crit(self.roll.count(await dice.getFloorNumber()), criticalFailureMessage, criticalFailureReactions)

        return self
    
    async def processOptionsReturnFinalStatement(self, dice):
        # 0 -> Reroll values
        # 1 -> Keep dice out of the roll
        # 2 -> Target number for a success
        # 3 -> Target number for a failure
        final = await calculateFinalSum(self.roll)
        
        for optionIndex, optionNumber in enumerate(dice.optionsFlags):
            if optionNumber is not None: 
                if optionIndex == Options.KeepDice:                  
                    self.roll = await processKeepOption(self.roll, optionNumber)
                    final = await self.calculateFinalSum(self.roll)
                #Fill out the rest
                
            await asyncio.sleep(0.02)
                
        return final

    
    async def crit(self, totalNumbCrits, critMessage, reactionsToAdd):
        """ Celebrative message for the Critical hit """
        critTimesStr = await self.getCriticalString(totalNumbCrits)

        msg = await self.context.send(f'{self.context.author.mention} {critMessage} {critTimesStr}')
        await self.addReactions(msg, reactionsToAdd)

        return self


    async def addReactions(self, msg, reactions: tuple):
        for react in reactions:
            await msg.add_reaction(react)
            
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
    
    

async def critedSuccess(listOfRolls: list, dice) -> bool:
        """ In list_of_roll is there a maximum value? """
        return await dice.getCeilingNumber() in listOfRolls
    
async def critedFailure(listOfRolls, dice):
    return await dice.getFloorNumber() in listOfRolls