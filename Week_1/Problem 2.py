# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 06:43:19 2019

@author: Shobhit Kulshreshtha
"""

#Assume s is a string of lower case characters.
#
#Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:
#
#Number of vowels: 5

#Initialize a count variable
countBob = 0

#For testing let's define a string 's'. Delete before submission
s = 'azcbobobegghakl'

#checking all characters of string s
for n in range(len(s)):
    if s[n:n+3] == 'bob':
        countBob += 1

print('Number of times bob occurs is:',countBob)