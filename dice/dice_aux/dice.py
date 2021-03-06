import asyncio
import random

from .constant_dice import *
from ..helful_functions import *
from .error import Error
from ..options.options_modifiers import *


class Dice():
    async def getFloorNumber(self):
        return eval(f'{STARTROLL}{self.modifiers}')
        
    async def getCeilingNumber(self):
        return eval(f'{self.typeDice}{self.modifiers}')
    
    async def getModifiedNumber(self, number: int):
        return eval(f'{number}{self.modifiers}')
    
    
    async def rolling(self):
        rolls = list()
        for _ in range(self.numDice):
            rolls.append(await self.getModifiedNumber(random.randint(STARTROLL, self.typeDice)))
            
        return rolls
    
    
    async def createCustomDice(self, numDice, typeDice, modifiers, optionsFlags):
        if numDice:
            try: 
                self.numDice = int(numDice)
            except ValueError: return await Error().defineError("Custom Dice information not introduced properly.")

            if not self.validDiceInfo(numDice): return await Error().defineError("Custom Dice information not introduced properly.")
                
        else: return await Error().defineError("Custom Dice information not introduced properly.")
        
        if typeDice:
            try: 
                self.typeDice = int(typeDice)
            except ValueError: return await Error().defineError("Custom Dice information not introduced properly.")

            if not self.validDiceInfo(typeDice): return await Error().defineError("Custom Dice information not introduced properly.")
        else: return await Error().defineError("Custom Dice information not introduced properly.")
        
        if modifiers:
            if isinstance(modifiers, Modifier): self.modifiers = modifiers
            else: return await Error().defineError("Custom Dice information not introduced properly.")
        else: self.modifiers = None
            
        if optionsFlags:
            if isinstance(optionsFlags, Options): self.optionsFlags = optionsFlags
            else: return await Error().defineError("Custom Dice information not introduced properly.")
        else: self.optionsFlags = None

        return self
                
    async def processInputDice(self, _input):
        
        processedInput = await self.processRawInput( _input)
        
        if len(processedInput["dice"]) == 1:
            # At least two components, number of Dice and type of Dice
            return await Error().defineError("Dice information not introduced properly.")
        
        dice = await self.processDiceInfo(processedInput["dice"])
        if isinstance(dice, Error): return dice
        
        self.numDice, self.typeDice = dice["numDice"], dice["typeDice"]
        # basic dice information defined
        
        options = await self.processDiceOptions(processedInput["options"])
        if isinstance(options, Error): return options
        
        self.modifiers, self.optionsFlags = options["modifiers"], options["optionsFlags"]
        
        return self
        
        
        
    async def processDiceOptions(self, optionsInput):
        optionsFlags = await Options().initOptionFlags()
        modifiers = await Modifier().initModifier()
        
        state = inputOptionsState.searching
        
        for option in optionsInput:
            for char in option:
                
                if state is inputOptionsState.receivingAndStoringOptions:
                    if await isNumber(char): await optionsFlags.addCharacter(optionIndex, char)
                        # State stays the same
                    else: state = inputOptionsState.searching
                
                elif state is inputOptionsState.receivindAndStoringModifier: 
                    if await isNumber(char): await modifiers.addCharacter(char)
                        # State stays the same
                    else: state = inputOptionsState.searching
                        
                        
                if state is inputOptionsState.searching:                 
                    if char in Operators:
                        await modifiers.addCharacter(char)
                        state = inputOptionsState.foundModifier
                        
                    elif char in AllOptions: optionIndex = await optionsFlags.getOptionsIndex(char)
                    
                    if char in OptionsOutNumber: state = inputOptionsState.foundOption
                        
                    elif char in OptionsWithNumber:
                        state = inputOptionsState.receivingAndStoringOptions
                
                elif state is inputOptionsState.foundModifier:   
                    if await isNumber(char):
                        await modifiers.addCharacter(char)
                        state = inputOptionsState.receivindAndStoringModifier
                    else: return await Error().defineError("Options wrongly formated")
                    
                elif state is inputOptionsState.foundOption:
                    if await isNumber(char):
                        await optionsFlags.setOption(optionIndex, char)
                        state = inputOptionsState.receivingAndStoringOptions
                    else: return await Error().defineError("Options wrongly formated")
                    
                await asyncio.sleep(0.02)
        
        if state is inputOptionsState.foundModifier or state is inputOptionsState.foundOption:
            return await Error().defineError("Options wrongly formated")
        else: return {"modifiers": modifiers.value, "optionsFlags": optionsFlags.optionsFlags}
    
    
    async def processRawInput(self, _input) -> dict:
        processedInput = dict()
        processedInput["dice"] = _input[0].lower()
        processedInput["dice"] = processedInput["dice"].split(DiceKeyLetter)
        
        processedInput["options"] = _input[1:]
        
        return processedInput
        
        
    async def processDiceInfo(self, diceInput) -> dict:
        diceInfo = dict()
    
        diceInfo["numDice"] = await self.processNumberOfDice(diceInput[0])
        if isinstance(diceInfo["numDice"], Error): return diceInfo["numDice"]

        diceInfo["typeDice"] = await self.processTypeOfDice(diceInput[1])
        if isinstance(diceInfo["typeDice"], Error): return diceInfo["typeDice"]
        
        return diceInfo
    
    
    async def processTypeOfDice(self, typeDiceInput) -> int:
        typeDice = typeDiceInput
        
        try:
            typeDice = int(typeDice)
        except ValueError:
            return await Error().defineError("Dice information not introduced properly.")
        
        if not await self.validDiceInfo(typeDice): return await Error().defineError("Dice information not introduced properly.")
        return typeDice
    
    
    async def processNumberOfDice(self, numDiceInput) -> int:
        if numDiceInput == EMPTYSTRING: numDice = 1
        else:
            try:
                numDice = int(numDiceInput)
            except ValueError:
                return await Error().defineError("Dice information not introduced properly.")

        if not await self.validDiceInfo(numDice): return await Error().defineError("Dice information not introduced properly.")
        return numDice
        
    async def validDiceInfo(self, info: int) -> bool:
        return info > 0