# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 03:30:50 2018

@author: Carlos Isaac
"""
test = (5, (1,2), [[1],[[3,6],[7,9,[5,8,[10,50,[110,1]]]]]])

from collections import Iterable

def FlatList(aList):
    """Yield items from any nested iterable; see REF."""
    for entry in aList:
        if isinstance(entry, Iterable):
            yield from FlatList(entry)
        else:
            yield entry

def max_val(t): 
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    L = list(FlatList(t))
    return max(L)

                
            
print(max_val(test))
