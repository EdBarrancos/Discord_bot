from enum import Enum

class inputOptionsState(Enum):
    searching = 0
    foundModifier = 1
    foundOption = 2
    receivindAndStoringModifier = 3
    receivingAndStoringOptions = 4
    
    async def initOptionsState(self):
        return inputOptionsState().searching


class Options():
    async def initOptionFlags(self):
        self.optionsFlags = list()
        for _ in range(NumberOfOptions):
            self.optionsFlags.append(None)
            
        return self
    
    async def addCharacter(self, index, char):
        self.optionsFlags[index] += char
        return self
    
    async def getOptionsIndex(self, char):
        index = AllOptions.index(char)
        if char in OptionsOutNumber:
            await self.optionsFlags.setOption(index, ACTIVE)
        
        return index
    
    async def setOption(self, index, setValue):
        self.optionsFlags[index] = setValue
        return self
    

    class Modifier():
        async def initModifier(self):
            self.value = EMPTYSTRING
            return self
        
        async def addCharacter(self, char):
            self.value += char
            return self

ACTIVE = "1"
EMPTYSTRING = ''

Operators = "+-/*"

OptionsWithNumber = "krtf"
# Needs somesort of number
OptionsOutNumber = ""
#Doesnt require number

AllOptions = OptionsWithNumber + OptionsOutNumber

NumberOfOptions = len(AllOptions)