""" 
    File: dice.py
    Author: Eduardo Barrancos
    Description: Manage the dice related funcitons
"""
import random

from .dice_aux.dice import Dice
from .dice_aux.error import Error
from .constant_dice_main import *
from .dice_aux.helful_functions import *
from .quicksort import quicksort


class Roll:
    async def roll_dice(self, context, _input, helpCommand='help'):
        """ To add an Option:
            Expect a new index in the tuple
            Add a new index and the condicitons for it in the flag
            Add it to help """          
        self.context = context
        self.helpCommand = helpCommand

        dice = Dice()
        await dice.processInputDice(_input)
        if isinstance(dice, Error): return dice.sendErrorToUser(self.context, self.helpCommand)

        self.roll = await self.rolling(dice)
        self.roll = await quicksort(self.roll, 0, len(self.roll) - 1, comparator=lambda a,b: a > b)

        finalStatement = await self.processOptions(dice)

        await self.context.send(f'{self.context.author.mention} rolled:`{self.roll}`. Which means:`{finalStatement}`')
        
        

        if await crited(self.roll, dice.typeDice, dice.modifier):
            await self.crit(self.roll.count(eval(f'{dice.typeDice}{dice.modifier}')))

        return self
    
    async def processOptions(self, dice):
        # 0 -> Keep dice out of the roll
        # 1 -> Reroll values
        # 2 -> Target number for a success
        # 3 -> Target number for a failure
        final = await calculateFinal(self.roll)
        for optionIndex, optionNumber in enumerate(dice.optionsFlags):
            if optionNumber is not None: 
                if optionIndex == 0:
                    self.roll = self.roll[:int(optionNumber)] # Make a Function for this
                    final = await self.calculateFinal(self.roll)
                #Fill out the rest
                
        return final
    
    async def calculateFinal(self, roll):
        return sum(roll)

    async def crit(self, totalNumbCrits):
        """ Celebrative message for the Critical hit """
        critTimesStr = f'{totalNumbCrits} times!'
        if totalNumbCrits == 1:
            critTimesStr = EMPTYSTRING

        msg = await self.context.send(f'F*** YEAH!! {self.context.author.mention} JUST CRITED! {critTimesStr}')
        await msg.add_reaction(StarStruck)
        await msg.add_reaction(MindBlowen)
        await msg.add_reaction(Cursing)
        await msg.add_reaction(PartyTime)

        return self


    async def rolling(self, dice):
        """ Returns a list with each individual rolls.
                self.numDice elements each from 1 to self.typeDice  """

        rolls = list()
        print(dice)
        print(dice.typeDice)
        for _ in range(dice.numDice):
            rolls.append(dice.getModifiedNumber(random.randint(STARTROLL, dice.typeDice)))
            await asyncio.sleep(0.02)
        return rolls
    
    

async def crited(listOfRolls: list, typeDice: str, modifier: str) -> bool:
        """ In list_of_roll is there a maximum value? """
        return eval(f'{typeDice}{modifier}') in listOfRolls  