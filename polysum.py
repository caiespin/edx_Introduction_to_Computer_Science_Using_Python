# -*- coding: utf-8 -*-
"""
Created on Mon May 28 17:32:43 2018

@author: Carlos Isaac
"""

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