# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 06:07:03 2018

@author: Carlos Isaac
"""
L = [1, 2, 3, 4]
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    def poly(x):
        res = 0
        exp = len(L)
        for item in L:
            exp -= 1
            res += item*(x**exp)
        return res
    return poly

print(general_poly (L)(10))