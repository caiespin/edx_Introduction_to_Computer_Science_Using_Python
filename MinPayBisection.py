# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 01:09:14 2018

@author: Carlos Isaac
PROBLEM SET 2

Calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month.

Formulas:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly payment lower bound = Balance / 12
Monthly payment upper bound = (Balance x (1 + Monthly interest rate)**12) / 12.0
"""

balance = 320000
annualInterestRate = 0.2

MonthInteRate = (annualInterestRate) / 12.0
lowerBound = balance/12
upperBound = (balance*((1 + MonthInteRate)**12)) / 12.0

monts = 12
tolerance = 0.01

def Debt(balance,monthlyPayment, MonthInteRate, months):
    '''
    balance: int or float.
    monthlyPaymentRate: int or float.
    MonthInteRate: int or float.
    months: int.
    
    returns: float two decimal digits of accuracy.
    '''
    if months <= 0:
        return round(balance, 2)
    else:
        MonthUnBal = balance - monthlyPayment
        UpdBalance = MonthUnBal + MonthInteRate*MonthUnBal
        return Debt(UpdBalance,monthlyPayment, MonthInteRate, months-1)
    
def MinPayBisection(lowerBound, upperBound, tolerance, MaxIter, IterCount,balance, MonthInteRate, months):
    '''
    lowerBound: int or float.
    upperBound: int or float.
    tolerance: int or float. 
    MaxIter: int 
    IterCount: int
    balance: int or float.
    monthlyPaymentRate: int or float.
    MonthInteRate: int or float.
    months: int.
    
    returns: float two decimal digits of accuracy.
    '''
    FA = Debt(balance,lowerBound, MonthInteRate, months)
    Intermidpoint = ((upperBound-lowerBound)/2)
    Aproximation = lowerBound + Intermidpoint
    FR = Debt(balance,Aproximation, MonthInteRate, months)
    if IterCount >= MaxIter:
        print('\n Method Failed')
        return 0
    if FR==0 or Intermidpoint<tolerance:
        return round(Aproximation, 2)
    if FA*FR > 0:
        return MinPayBisection(Aproximation, upperBound, tolerance, MaxIter, IterCount+1,balance, MonthInteRate, months)
    else:
        return MinPayBisection(lowerBound, Aproximation, tolerance, MaxIter, IterCount+1,balance, MonthInteRate, months)
    
    
print('Lowest Payment: '+str(MinPayBisection(lowerBound, upperBound, tolerance, 1000, 1,balance, MonthInteRate, 12)))

