# -*- coding: utf-8 -*-
"""
Created on Sun May 27 17:10:48 2018

@author: Carlos Isaac
"""

def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    power=1
    while exp>0:
        power = power*base
        exp -= 1
    return power

print(iterPower(5,0))

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recurPower(base, exp-1)
    
print(recurPower(5,0))

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    rem = 1
    rem1 = 1
    if a < b:
        test = a
        while rem > 0 or rem1 > 0:
            rem = b%test
            rem1 = a%test
            result = test
            test -= 1
        return result
    else:
        test = b
        while rem > 0 or rem1 > 0:
            rem = a%test
            rem1 = b%test
            result = test
            test -= 1
        return result
    
def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
    
str1 = 'abcdefghijklmnopqrtuvwxyz'
mid1 = len(str1)//2  
  
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    mid = len(aStr)//2
    if len(aStr) == 0:
        return False
    if len(aStr) == 1 and char == aStr:
        return True
    elif len(aStr) == 1 and char != aStr:
        return False
    elif char == aStr[mid]:
        return True
    elif char < aStr[mid]:
        return isIn(char, aStr[:mid])
    elif char > aStr[mid]:
        return isIn(char, aStr[mid:])
        
import math

def polysum(n, s):
    '''
    Calculate the sum of the area and the square of the perimeter of the 
    a regular polygon.
    n: positive integer. 
    s: int or float.
    
    Returns float rounded to 4 decimal places.
    '''
    perimeter = n * s
    area = (0.25*n*(s**2))/(math.tan(math.pi/n))
    result = area + (perimeter**2)
    return round(result, 4)
    