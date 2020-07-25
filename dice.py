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

        print(_input)
        dice = _input[0]
        dice = dice.split('d')
        if len(dice) == 1:
            #Input not formated properly
            await self.somethingWentWrong("Dice information not introduced properly.")
        else:
            print('in progress')
        return self

    # async def getDiceInfo(self, dice)
    async def somethingWentWrong(self, errorMessage):
        await self.guild.send(errorMessage)
        await self.guild.send(f'For more better imformation type {self.helpCommand}.')
