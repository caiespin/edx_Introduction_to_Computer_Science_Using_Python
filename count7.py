# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:51:09 2018

@author: Carlos Isaac
"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    if N <= 0:
        return 0
    else:
        if N%10 == 7:
            return count7(N//10) + 1
        else:
            return count7(N//10)
        

    