from ..dice_aux.dice import Dice
from ..dice_aux.error import Error
from ..helful_functions import findIndexes, deleteIndexes
from ..quicksort import sort, sortingDirection
from ..constant_dice_main import TargetNumberSuccessReactions, TargetNumberFailureReactions

async def processKeepOption(vector: list, number) -> list:
    return processedOutput(roll = vector[:int(number)], finalMessage = calculateFinalSum(vector))
 
 
async def processRerollValues(vector, number, dice):
    rerollIndexes = await findIndexes(vector, number)
    vector = await deleteIndexes(vector, listOfIndexes)
    auxiliaryDice = Dice().createCustomDice(len(rerollIndexes), dice.typeDice, dice.modifiers, None)
    if isinstance(auxiliaryDice, Error): return auxiliaryDice
    
    vector += auxiliaryDice.rolling()
    
    vector = await sort(vector, sortingDirection.biggestToLowest)
    return processedOutput(roll = vector, finalMessage = calculateFinalSum(vector))
    

async def processTargetNumberSuccess(vector, number):
    finalMessage = FailureMessage
    reactions = TargetNumberFailureReactions
    if number in vector:
        finalMessage = TargetNumberSuccessMessage
        reactions = TargetNumberSuccessReactions

    return processedOutput(roll = vector, finalMessage = finalMessage, reactions = reactions)

async def processTargetNumberFailure(vector, number):
    finalMessage = FailureMessage
    reactions = TargetNumberSuccessReactions
    if number in vector:
        finalMessage = TargetNumbeFailureMessage
        reactions = TargetNumberFailureReactions

    return processedOutput(roll = vector, finalMessage = finalMessage, reactions = reactions)


async def calculateFinalSum(roll: list) -> int:
        return sum(roll)


class processedOutput:
    async def create(roll = [], finalMessage = "", reactions = ()):
        self.roll = roll
        self.finalMessage = finalMessage
        self.reactions = reactions
    


###########
# Options #
###########

RerollValues = 0
KeepDice = 1
TargetNumberSuccess = 2
# TargetNumberSucess Message:
TargetNumberSuccessMessage = "You succeeded. Congrats!"
TargetNumberFailure = 3
# TargetNumberfailure Message:
TargetNumberFailureMessage = "You Failed. You Suck! Sorry."

# Target Failure:
FailureMessage = "Sorry"