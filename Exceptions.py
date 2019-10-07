# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 21:45:05 2018

@author: Carlos Isaac
"""
def fancy_divide(list_of_numbers, index):
   denom = list_of_numbers[index]
   return [simple_divide(item, denom) for item in list_of_numbers]


def simple_divide(item, denom):
    try:
        return item / denom
    except ZeroDivisionError:
        return 0


#def fancy_divide(list_of_numbers, index):
#    try:
#        try:
#            raise Exception("0")
#        finally:
#            denom = list_of_numbers[index]
#            for i in range(len(list_of_numbers)):
#                list_of_numbers[i] /= denom
#    except Exception as ex:
#        print(ex)
        
print(fancy_divide([0, 2, 4], 5))