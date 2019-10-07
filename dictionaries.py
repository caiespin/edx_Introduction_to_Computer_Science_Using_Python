# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 02:47:15 2018

@author: Carlos Isaac
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for entry in aDict:
        count += len(aDict[entry])
    return count

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxim = 1
    res = None
    for entry in aDict:
        if maxim < len(aDict[entry]):
            res = entry
            maxim = len(aDict[entry])
    return res

print(biggest(animals))