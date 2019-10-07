# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 23:12:40 2018

@author: Carlos Isaac
"""

def cipher2(map_from, map_to, code):
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
    mapfrom = list(map_from)
    mapto = list(map_to)

    for i in range(len(mapfrom)):
        key_code[mapfrom[i]] = mapto[i]
    
    decoded = []

    for letter in list(code):
        decoded.append(key_code[letter])
     
    return key_code, ''.join(decoded)