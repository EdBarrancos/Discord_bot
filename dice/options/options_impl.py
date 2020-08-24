from ..dice_aux.dice import Dice
from ..dice_aux.error import Error
from ..helful_functions import findIndexes, deleteIndexes

async def processKeepOption(vector: list, number) -> list:
    return vector[:int(number)]
 
 
async def processRerollValues(vector, number, dice):
    rerollIndexes = await findIndexes(vector, number)
    vector = await deleteIndexes(vector, listOfIndexes)
    auxiliaryDice = Dice().createCustomDice(len(rerollIndexes), dice.typeDice, dice.modifiers, None)
    if isinstance(auxiliaryDice, Error): return auxiliaryDice
    
    vector += auxiliaryDice.rolling()
    
    return vector
    
    
async def calculateFinalSum(roll: list) -> int:
        return sum(roll)
    

###########
# Options #
###########

RerollValues = 0
KeepDice = 1
TargetNumberSuccess = 2
TargetNumberFailure = 3