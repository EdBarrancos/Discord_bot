from enum import Enum
from .constant_options import *

class inputOptionsState(Enum):
    searching = 0
    foundModifier = 1
    foundOption = 2
    receivindAndStoringModifier = 3
    receivingAndStoringOptions = 4


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
            await self.setOption(index, ACTIVE)
        elif self.isEmpty(index):
            await self.setOption(index, EMPTYSTRING)
        
        return index
    
    async def setOption(self, index, setValue):
        self.optionsFlags[index] = setValue
        return self
    
    async def isEmpty(self, idnex):
        return  self.optionsFlags[index] == None
    

class Modifier():
    async def initModifier(self):
        self.value = EMPTYSTRING
        return self
    
    async def addCharacter(self, char):
        self.value += char
        return self
