from enum import Enum

async def processKeepOption(vector: list, number) -> list:
    return vector[:int(number)]
    
    
async def calculateFinalSum(roll: list) -> int:
        return sum(roll)
    

ReerollValues = 0
KeepDice = 1
TargetNumberSuccess = 2
TargetNumberFailure = 3
    