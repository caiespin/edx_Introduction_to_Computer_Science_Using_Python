# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 02:14:13 2018

@author: Carlos Isaac
"""

test = { 'b': 1, 'c': 2, 'a': 3, 'd': 1, 'e': 2, 'f': 3, 'g': 1, 'h': 2, 'i': 4}



def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    Vals = []
    res = []
    for entry in aDict:
        Vals.append(aDict[entry])
    unique = list(set(Vals)) 
    for entry in unique:
        Vals.remove(entry)
    for entry in Vals:
        if entry in unique:
            unique.remove(entry)
    for entry in aDict:        
        if aDict[entry] in unique:
            res.append(entry)
            unique.remove(aDict[entry])
    res.sort()
    return res

print(uniqueValues(test))
          