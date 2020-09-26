import random
import asyncio

from .dice_aux.dice import Dice
from .dice_aux.error import Error
from .constant_dice_main import *
from .helful_functions import *
from .quicksort import sort, sortingDirection
from .options.options_impl import *


class Roll:
    async def roll_dice(self, context, _input: tuple, helpCommand='help'):
        """ Outputs random values according to user input """          
        self.context = context
        self.helpCommand = helpCommand

        dice = Dice()
        dice = await dice.processInputDice(_input)
        if isinstance(dice, Error): 
            return await dice.sendErrorToUser(self.context, self.helpCommand)

        self.roll = await dice.rolling()
        self.roll = await sort(self.roll, sortingDirection.biggestToLowest)

        finalStatement = await self.processOptionsReturnFinalStatement(dice)

        await self.sendOutputMessage(finalStatement)

        if await critedSuccess(self.roll, dice):
            await self.sendCritMessageAndReaction(self.roll.count(await dice.getCeilingNumber()), criticalSuccessMessage, criticalSuccessReactions)
            
        if await critedFailure(self.roll, dice):
            await self.sendCritMessageAndReaction(self.roll.count(await dice.getFloorNumber()), criticalFailureMessage, criticalFailureReactions)

        return self
    

    async def sendOutputMessage(self, outputObject):
        msg = await self.context.send(f'{self.context.author.mention}')
        if outputObject.roll:
            msg = await self.context.send(f'Rolled: `{outputObject.roll}`')
        if outputObject.finalMessage:
            msg = await self.context.send(f'Which Means: `{outputObject.finalMessage}`')
        if outputObject.reactions:
            await self.addReactions(msg, outputObject.reactions)


    async def processOptionsReturnFinalStatement(self, dice: Dice) -> int:
        # 0 -> Reroll values
        # 1 -> Keep dice out of the roll
        # 2 -> Target number for a success
        # 3 -> Target number for a failure
        final = await calculateFinalSum(self.roll)
        
        for optionIndex, optionNumber in enumerate(dice.optionsFlags):
            if optionNumber is not None: 
                if optionIndex == KeepDice:       
                    final = await processKeepOption(self.roll, optionNumber)
 
                elif optionIndex == RerollValues:
                   final = await processRerollValues(self.roll, optionNumber, self.dice)

                elif optionIndex == TargetNumberSuccess:
                    final = await processTargetNumberSuccess(self.roll, optionNumber)

                elif optionIndex == TargetNumberFailure:
                    final = await processTargetNumberFailure(self.roll, optionNumber)

                #Fill out the rest
                
            await asyncio.sleep(0.02)
                
        return final

    
    async def sendCritMessageAndReaction(self, totalNumbCrits: int, critMessage: str, reactionsToAdd: tuple):
        """ Celebrative message for the Critical hit """
        critTimesStr = await self.getCriticalString(totalNumbCrits)

        msg = await self.context.send(f'{self.context.author.mention} {critMessage} {critTimesStr}')
        await self.addReactions(msg, reactionsToAdd)

        return self


    async def addReactions(self, msg, reactions: tuple):
        for react in reactions:
            await msg.add_reaction(react)
            
        return self
    
    
    async def getCriticalString(self, totalNumbCrits: int) -> str:
        criticalString = f'{totalNumbCrits} times!'
        if totalNumbCrits == 1: criticalString = EMPTYSTRING
        
        return criticalString    
    

async def critedSuccess(listOfRolls: list, dice: Dice) -> bool:
        return await dice.getCeilingNumber() in listOfRolls
    
async def critedFailure(listOfRolls: list, dice: Dice) -> bool:
    return await dice.getFloorNumber() in listOfRolls