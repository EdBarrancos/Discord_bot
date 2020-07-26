""" 
    File: dice.py
    Author: Eduardo Barrancos
    Description: Manage the dice related funcitons
"""
import asyncio

class Dice:
    async def create(self, ctx, _input, helpCommand='help'):
        self.guild = ctx
        self.helpCommand = helpCommand

        dice = _input[0]
        dice = dice.split('d')
        print(dice)
        if len(dice) == 1:
            #Input not formated properly
            await self.somethingWentWrong("Dice information not introduced properly.")
        else:
            if dice[0] == '':
                self.numDice = 1
            else:
                try:
                    self.numDice = int(dice[0])
                except ValueError:
                    await self.somethingWentWrong("Dice information not introduced properly.")
                    return self
            
            self.typeDice = ''
            i = 0
            while i < len(dice[1]) and (dice[1][i] >= '0' and dice[1][i] <= '9'):
                self.typeDice += dice[1][i]
                i += 1
            
            try:
                self.typeDice = int(self.typeDice)
            except ValueError:
                await self.somethingWentWrong("Dice information not introduced properly.")
                return self

            self.options = dice[1][i:]
            for rest in range(1,len(_input)):
                self.options += _input[rest]

            await self.guild.send(f'number of dice: {self.numDice}\n Number of dice: {self.typeDice}\n Options: {self.options}.')
        return self

    async def getDiceInfo(self, dice):
        """ Finds the number of dice and the type. 
            Returns the rest of the information """

    async def somethingWentWrong(self, errorMessage):
        """ Sends a error message and inputs the help command """
        await self.guild.send(errorMessage)
        await self.guild.send(f'For more better imformation type {self.helpCommand}.')
