# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:12:13 2018

@author: Carlos Isaac
"""

test = [2, 2, 4, 4]
test2 = 'a'

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    vowels = 'aeiouAEIOU'
    check = list(s)
    result = check[:]
    for letter in check:
        if letter in vowels:
            result.remove(letter)
    print(''.join(result))



def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """     
    check = {}
    check = check.fromkeys(L)
    for entry in check:
        check[entry] = 0
    for entry in L:
        check[entry] += 1
    result = check.copy()
    for entry in check:
        if check[entry]%2 == 0:
            result.pop(entry)
    if len(result) == 0:
        return None
    else:
        return max(result)

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    key_code = {}
    key_code = key_code.fromkeys(map_from)
    mapto = list(map_to)
    iterator = 0
    for entry in key_code:
        key_code[entry] = mapto[iterator]
        iterator += 1
    coded = list(code)
    decoded = coded[:]
    iterator = 0
    for entry in coded:
        decoded[iterator] = key_code[entry]
        iterator += 1
    decoded = ''.join(decoded)
    return key_code.copy(), decoded[:]

x, y = cipher("abcd", "dcba", "dab")

print(x, y)
