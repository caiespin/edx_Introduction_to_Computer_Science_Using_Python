# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 23:44:57 2018

@author: Carlos Isaac

PROBLEM SET 2

Calculate the credit card balance after one year if a person only pays 
the minimum monthly payment required by the credit card company each month.

Formulas:
Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) 
                           + (Monthly interest rate x Monthly unpaid balance)
"""

balance = 3926
annualInterestRate = 0.2

MonthInteRate = (annualInterestRate) / 12.0
months = 12


def Debt(balance,monthlyPayment, MonthInteRate, months):
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
        MonthUnBal = balance - monthlyPayment
        UpdBalance = MonthUnBal + MonthInteRate*MonthUnBal
        return Debt(UpdBalance,monthlyPayment, MonthInteRate, months-1)
    
def Payments(balance,monthlyPayment, MonthInteRate, months):
    '''
    balance: int or float.
    monthlyPaymentRate: int or float.
    MonthInteRate: int or float.
    months: integer.
    
    returns: integer.
    '''
    Currentbalance = Debt(balance,monthlyPayment, MonthInteRate, months)
    if Currentbalance <= 0:
        return monthlyPayment
    else:
        return Payments(balance,monthlyPayment + 10, MonthInteRate, months)
    
    
print('Lowest Payment: '+str(Payments(balance,0, MonthInteRate, months)))