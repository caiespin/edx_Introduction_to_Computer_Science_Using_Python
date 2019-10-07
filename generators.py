# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 21:35:16 2018

@author: Carlos Isaac
"""
def genFib():
	fibn_1 = 1
	fibn_2 = 2
	while True:
		next = fibn_1 + fibn_2
		yield next
		fibn_2 = fibn_1
		fibn_1 = next
        
def genPrimes():
    """
    Have the generator keep a list of the primes it's generated. 
    A candidate number x is prime if (x % p) != 0 for all earlier primes p.
    """
    primes = []
    count = 1
    summ = 0
    while True:
        for num in primes:
            summ *= count%num
        if summ != 0:
            primes.append(count)
            next = primes
            yield next
        count += 1
        summ = 1
        
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

def genPrimes_sol():
    primes = []   # primes generated so far
    last = 1      # last number tried
    while True:
        last += 1
        for p in primes:
            if last % p == 0:
                break
        else:
            primes.append(last)
            yield last
        
        
    