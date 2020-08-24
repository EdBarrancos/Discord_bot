async def isNumber(st: str) -> bool:
    """ Checks if a string is a number string """
    return st >= "0" and st <= "9"

async def findIndexes(vector: list, element) -> list:
    indexesList = list()
    
    for index, ele in enumerate(vector):
        if ele == element: indexesList.append(index)
        
    return indexesList

async def deleteIndexes(vector: list, indexesToDelete; list) -> list:
    for index in indexesToDelete: 
        del vector[index]
        
    return vector
    
    
    