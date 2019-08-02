# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 07:16:58 2019

@author: Shobhit Kulshreshtha
"""

# =============================================================================
#Problem 2 - Paying Debt Off in a Year
#0.0/15.0 points (graded)
#Now write a program that calculates the minimum fixed monthly payment needed 
# in order pay off a credit card balance within 12 months. By a fixed monthly payment,
# we mean a single number which does not change each month, but instead is a constant
# amount that will be paid each month.
#
#In this problem, we will not be dealing with a minimum monthly payment rate.
#
#The following variables contain values as described below:
#
#balance - the outstanding balance on the credit card
#
#annualInterestRate - annual interest rate as a decimal
#
#The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year, for example:
#
#Lowest Payment: 180 
#Assume that the interest is compounded monthly according to the balance at the end of the month (after the payment for that month is made). The monthly payment must be a multiple of $10 and is the same for all months. Notice that it is possible for the balance to become negative using this payment scheme, which is okay. A summary of the required math is found below:
#
#Monthly interest rate = (Annual interest rate) / 12.0
#Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
# =============================================================================

balance = 4773
annualInterestRate = 0.2


#Defining a function to calculate lowest payment
def lowest_payment(n, bal, AIR):
    '''
    n: number of months (int)
    bal: Initial debt amount (int or float)
    AIR: Annual Interest Rate (float)
    
    Returns the lowest monthly payment (float) required to settle the balance at the end of n months
    '''

    monthlyInterestRate = AIR / 12.0
    
    #Can mathematically calculate that lowest payment, P, is equal to 
    #       P = B * (1+MIR)**n / ((1+MIR)**n + (1+MIR)**n-1 + ..... + (1+MIR))
    def denom_GP(m, MIR):
        '''
        m:number of months (int)
        MIR: Monthly Interest Rate (float)
        
        Returns the value (float) of denominator Geometric progression showcased in comment above
        '''
        if m == 1:
            return 1+MIR
        else:
            return ((1+MIR)**m + denom_GP(m-1, MIR))

    lowestPayment = (bal * ((1 + monthlyInterestRate) ** n)) / denom_GP(n, monthlyInterestRate)
    
    if round(lowestPayment) % 10 <= 5.0:
        lowestPayment = round(round(lowestPayment,-1)+10)
    else:
        lowestPayment = round(lowestPayment,-1)
    return lowestPayment

#Invoking function & storing lowest payment in a variable
minimumPayment = lowest_payment(12,balance,annualInterestRate)

print("Lowest Payment: " + str(minimumPayment))