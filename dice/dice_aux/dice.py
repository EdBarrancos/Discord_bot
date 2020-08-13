import sys
sys.path.append('../')

from constant_dice import *
from helful_functions import *
from error import Error
from options.options import *


class Dice():
    async def processInputDice(self _input):
        processedInput = await processRawInput(self, _input)
        if len(processedInput["dice"]) == 1:
            # At least two components, number of Dice and type of Dice
            return await Error().defineError("Dice information not introduced properly.")
        
        dice = self.getDiceInfo(processedInput["dice"])
        if isinstance(dice, Error):
            error = dice 
            return error
        
        self.numDice, self.typeDice = dice["numDice"], dice["typeDice"]
        # basic dice information defined
        
        
        
    async def getDiceOptions(self, optionsInput):
        optionsFlag = await Options().initOptionFlags()
        modifiers = await Modifier().initModifier()
        
        state = await inputOptionsState().initOptionsState()
        
        for char in optionsInput:
            if state is inputOptionsState().receivingAndStoringOptions:
                if await isNumber(char): await optionsFlags.addCharacter(optionIndex, char)
                    # State stays the same
                else: state = inputOptionsState().searching
            
            elif state is inputOptionsState().receivindAndStoringModifier:
                if await isNumber(char): await modifiers.addCharacter(char)
                    # State stays the same
                else: state = inputOptionsState().searching
                    
                    
            if state is inputOptionsState().searching:
                if char in Operators:
                    await modifiers.addCharacter(char)
                    state = inputOptionsState().foundModifier
                    
                elif char in AllOptions:
                    optionIndex = optionsFlags.getOptionsIndex(char)
                
                if char in OptionsOutNumber:
                    state = inputOptionsState().foundOption
                    
                elif char in OptionsWithNumber:
                    state = inputOptionsState().receivingAndStoringOptions
            
            elif state is inputOptionsState().foundModifier:
                if await isNumber(char):
                    modifiers.addCharacter(char)
                    state = inputOptionsState().receivindAndStoringModifier
                else: return await Error().defineError("Options wrongly formated")
                
            elif state is inputOptionsState().foundOption:
                if await isNumber(char):
                    optionsFlags.setOption(optionIndex, char)
                    state = inputOptionsState().receivingAndStoringOptions
                else: return await Error().defineError("Options wrongly formated")
                
        if state is inputOptionsState().foundModifier or state is inputOptionsState().foundOption:
            return await Error().defineError("Options wrongly formated")
        else: return {"modifiers": modifiers, "optionsFlags": optionsFlags}
    
    
    async def processRawInput(self, _input):
        processedInput = dict()
        processedInput["dice"] = _input[0].lower()
        processedInput["dice"] = processedInput["dice"].split(DiceKeyLetter)
        
        processedInput["options"] = _input[1:]
        
        return processedInput
        
        
    async def getDiceInfo(self, diceInput):
        diceInfo = dict()
    
        diceInfo["numDice"] = self.getNumberOfDice(diceInput[0])
        if isinstance(diceInfo["numDice"], Error):
            error = diceInfo["numDice"]
            return error

        diceInfo["typeDice"] = self.getTypeOfDice(diceInput[1])
        if isinstance(diceInfo["typeDice"], Error):
            error = diceInfo["typeDice"]
            return error
        
        return diceInfo
    
    
    async def getTypeOfDice(self, typeDiceInput):
        typeDice = typeDiceInput
        
        try:
            typeDice = int(typeDice)
        except ValueError:
            return await Error().defineError("Dice information not introduced properly.")
        
        if not self.validDiceInfo(typeDice): return await Error().defineError("Dice information not introduced properly.")
    
    
    async def getNumberOfDice(self, numDiceInput):
        if numDiceInput == EMPTYSTRING:
            numDice = 1
        else:
            try:
                numDiceInput = int(numDiceInput)
            except ValueError:
                return await Error().defineError("Dice information not introduced properly.")

        if not self.validDiceInfo(numDice): return await Error().defineError("Dice information not introduced properly.")
        
    async validDiceInfo(self, info):
        return info > 0
    

    
