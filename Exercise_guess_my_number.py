# -*- coding: utf-8 -*-
"""
Spyder Editor

In this problem, you'll create a program that guesses a secret number!

The program works as follows: you (the user) thinks of an integer between 0 
(inclusive) and 100 (not inclusive). The computer makes guesses, and you give
it input - is its guess too high or too low? Using bisection search, the 
computer will guess the user's secret number!
"""
inst="Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."
high=100
low=0
guess=(high+low)//2
print("Please think of a number between 0 and 100!")
print("Is your secret number 50?")
answer=input(inst)
while True:
    if answer!='h' and answer!='l' and answer!='c':
        print("Sorry, I did not understand your input.")
        print("Is your secret number "+str(guess)+"?")
        answer=input(inst)
    if answer == 'h':
        high=guess
        guess=(high+low)//2
        print("Is your secret number "+str(guess)+"?")
        answer=input(inst)
    if answer == 'l':
        low=guess
        guess=(high+low)//2
        print("Is your secret number "+str(guess)+"?")
        answer=input(inst)
    if answer == 'c':
        print("Game over. Your secret number was:", guess)
        break
    
    