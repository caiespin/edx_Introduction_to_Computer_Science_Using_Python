# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 02:06:14 2018

@author: Carlos Isaac
"""
aList = ["apple", "cat", "dog", "banana"]

def lessThan4(aList):
    '''
    aList: a list of strings
    '''
    result = []
    for entry in aList:
        if len(entry) < 4:
            result.append(entry)
    return result
        



print(lessThan4(aList))