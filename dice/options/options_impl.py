from enum import Enum

async def processKeepOption(vector, number):
    
    print(id(vector))
    
    vector =  vector[:int(number)]
    return await calculateFinal(vector)
    
    
async def calculateFinalSum( roll):
        return sum(roll)
    
class Options(Enum):
    ReerollValues = 0
    KeepDice = 1
    TargetNumberSuccess = 2
    TargetNumberFailure = 3
    