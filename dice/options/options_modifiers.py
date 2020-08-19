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
    
    async def addCharacter(self, index: int, char: str):
        self.optionsFlags[index] += char
        return self
    
    async def getOptionsIndex(self, char: str) -> int:
        index = AllOptions.index(char)
        if char in OptionsOutNumber:
            await self.setOption(index, ACTIVE)
        elif await self.isEmpty(index):
            await self.setOption(index, EMPTYSTRING)
        
        return index
    
    async def setOption(self, index: int, setValue):
        self.optionsFlags[index] = setValue
        return self
    
    async def isEmpty(self, index: int) -> bool:
        return  self.optionsFlags[index] == None
    

class Modifier():
    async def initModifier(self):
        self.value = EMPTYSTRING
        return self
    
    async def addCharacter(self, char: str):
        self.value += char
        return self
