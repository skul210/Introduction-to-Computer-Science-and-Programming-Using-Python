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

#Defining a recursive function to check next character
def checkNext(line):
    if len(line) == 1:
        return line[0]
    else:
        char1 = line[0]
        char2 = line[1]
        if char1 <= char2:
            return char1+checkNext(line[1:])
        else:
            return char1

#For testing let's define a string 's'. Delete before submission
s = 'azcbobobegghakl'

#Initialize longest string
long_substr = ''

#checking all characters of string s
for n in range(len(s)):
    if len(checkNext(s[n:])) > len(long_substr):
        long_substr = checkNext(s[n:])

print('Longest substring in alphabetical order is:',long_substr)