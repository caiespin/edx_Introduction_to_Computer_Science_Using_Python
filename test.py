# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 23:51:09 2018

@author: Carlos Isaac
"""

#x = "pi"
#y = "pie"

stuff  = ["iQ"]
for thing in stuff:
        if thing == 'iQ':
           print("Found it")
           
           
def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x