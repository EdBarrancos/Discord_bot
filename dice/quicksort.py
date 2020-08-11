""" 
    File: quicksort.py
    Author: Eduardo Barrancos
    Description: QuickSort functions
"""
import  asyncio

async def quicksort(vector: list, left: int, right: int) -> list:
    """ QuickSort a list """
    if left < right:
        p = await particion(vector, left, right)
        vector = await quicksort(vector, left, p - 1)
        vector = await quicksort(vector, p + 1, right)
        
    return vector


async def particion(vector: list, left: int, right: int) -> int:
    pivot = vector[right]
    
    i = left - 1
    
    j = left
    for j in range(left, right):
        if await greater(vector[j], pivot): 
            i += 1
            vector[i], vector[j] = vector[j], vector[i]
    
    if await greater(pivot, vector[i + 1]): vector[i + 1], vector[right] = vector[right], vector[i + 1]
    
    return i + 1
        

    
async def greater(toTest, greater) -> bool:
    return toTest > greater