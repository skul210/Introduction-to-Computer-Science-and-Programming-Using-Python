# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 07:44:32 2019

@author: Shobhit Kulshreshtha
"""

low = 0
high = 100
guess = int((low + high)/2.0)


print('Please think of a number between 0 and 100!')
while(True):
    print('Is your secret number '+str(guess)+'?')
    g = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #Check for absurd inputs
    while g not in ['c','h','l']:
        print("Sorry, I did not understand your input.")
        g = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    #Bisection search
    if g == 'h':
        high = guess
        guess = int((low + high)/2.0)
    elif g == 'l':
        low = guess
        guess = int((low + high)/2.0)
    else:
        print("Game over. Your secret number was: "+str(guess))
        break