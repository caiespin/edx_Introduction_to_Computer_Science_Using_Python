# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:44:57 2018

@author: Carlos Isaac

PROBLEM SET 2

Calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month.

Formulas:
Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) 
                         + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 42
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

MonthInteRate = (annualInterestRate) / 12.0
months = 12


def Debt(balance,monthlyPaymentRate, MonthInteRate, months):
    '''
    balance: int or float.
    monthlyPaymentRate: int or float.
    MonthInteRate: int or float.
    months: integer.
    
    returns: float two decimal digits of accuracy.
    '''
    if months <= 0:
        return round(balance, 2)
    else:
        MonthUnBal = balance - monthlyPaymentRate*balance
        UpdBalance = MonthUnBal + MonthInteRate*MonthUnBal
        return Debt(UpdBalance,monthlyPaymentRate, MonthInteRate, months-1)
    
    
print('Remaining balance: '+str(Debt(balance,monthlyPaymentRate, MonthInteRate, months)))