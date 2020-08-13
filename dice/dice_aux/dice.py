import sys
sys.path.append('../')

from constant_dice import *
from helful_functions import *
from error import Error


class Dice():
    async def processInputDice(self, context, _input):
        self.context = context
        processedInput = await processRawInput(self, _input)
        if len(processedInput["dice"]) == 1:
            # At least two components, number of Dice and type of Dice
            return await Error().defineError("Dice information not introduced properly.")
        
        dice = self.getDiceInfo(processedInput["dice"])
        if isinstance(dice, Error):
            error = dice 
            return error
        else:
            return
        
    async def processRawInput(self, _input):
        processedInput = dict()
        processedInput["dice"] = _input[0].lower()
        processedInput["dice"] = processedInput["dice"].split(DiceKeyLetter)
        
        processedInput["options"] = _input[1:]
        
        return processedInput
        
        
    async def getDiceInfo(self, diceInput):
        diceInfo = dict()
    
        diceInfo["numberDice"] = self.getNumberOfDice(diceInput[0])
        if isinstance(diceInfo["numberDice"], Error):
            error = diceInfo["num"]
            return error

        

        return counter
    
    async def getTypeOfDice(self, typeDiceInput):
        typeDice = EMPTYSTRING
        counter = 0
        size_dice = len(typeDiceInput)
        while counter < size_dice and (await isNumber(typeDiceInput[counter])):
            typeDice += typeDiceInput[counter]
            counter += 1
        
        try:
            self.typeDice = int(self.typeDice)
        except ValueError:
            return await self.somethingWentWrong("Dice information not introduced properly.")
        
        if self.typeDice <= 0: return await self.somethingWentWrong("Dice information not introduced properly.")
    
    async def getNumberOfDice(self, numDiceInput):
        if numDiceInput == EMPTYSTRING:
            numDice = 1
        else:
            try:
                numDiceInput = int(numDiceInput)
            except ValueError:
                return await Error().defineError("Dice information not introduced properly.")

        if numDice <= 0: return await Error().defineError("Dice information not introduced properly.")
    