
from unittest import result
from test import counte
from itertools import permutations

#@njit(fastmath=True, cache=True)
        

def generat(arr):
    
    result = []
    for subset in permutations(arr, len(arr)): 
        result.append(subset)
    return result
    
