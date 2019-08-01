# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 07:16:58 2019

@author: Shobhit Kulshreshtha
"""

# =============================================================================
## Write a program to calculate the credit card balance after one year if a person only
# pays the minimum monthly payment required by the credit card company each month.
# 
# The following variables contain values as described below:
#
#balance - the outstanding balance on the credit card
#
#annualInterestRate - annual interest rate as a decimal
#
#monthlyPaymentRate - minimum monthly payment rate as a decimal
#
#For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print
#
#Remaining balance: 813.41
#instead of
#
#Remaining balance: 813.4141998135 
#So your program only prints out one thing: the remaining balance at the end of the year in the format:
#
#Remaining balance: 4784.0
#A summary of the required math is found below:
#
#Monthly interest rate= (Annual interest rate) / 12.0
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
# =============================================================================

balance = 484
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


#Defining a recursive function to calculate balance
def rem_balance(n,bal,AIR,MPR):
    '''
    n: number of months (int)
    bal: Initial debt amount (int or float)
    AIR: Annual Interest Rate (float)
    MPR: Minimum Payment Rate (float)
    
    Returns the total remaining balance (float) at the end of n months
    '''

    monthlyInterestRate = annualInterestRate / 12.0
    
    #Creating a base case
    if n == 1:
        unpaidBalance = bal * (1 - monthlyPaymentRate)
        return unpaidBalance * (1+monthlyInterestRate)
    else:
        minMonthlyPayment = monthlyPaymentRate * rem_balance(n-1,balance,monthlyInterestRate,monthlyPaymentRate)
        unpaidBalance = rem_balance(n-1,balance,monthlyInterestRate,monthlyPaymentRate) - minMonthlyPayment
        return round(unpaidBalance * (1 + monthlyInterestRate), 2)

#Invoking function & storing ending balance in a variable
end_balance = rem_balance(12,balance,annualInterestRate,monthlyPaymentRate)

print("Remaining balance: " + str(end_balance))