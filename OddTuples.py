# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 22:47:02 2018

@author: Carlos Isaac
"""
aTup = ('I', 'am', 'a', 'test', 'tuple')

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    res = ()
    for i in range(len(aTup)):
        if i%2 == 0:
            res = res + (aTup[i],)
    return res

def oddTuples2(aTup):
    '''
    Another way to solve the problem.
 
    aTup: a tuple
     
    returns: tuple, every other element of aTup. 
    '''
    # Here is another solution to the problem that uses tuple 
    #  slicing by 2 to achieve the same result
    return aTup[::2]

print(oddTuples(aTup))