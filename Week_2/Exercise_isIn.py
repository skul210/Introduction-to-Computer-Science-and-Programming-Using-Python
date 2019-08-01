# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if len(aStr) == 1:
        return char == aStr
    elif len(aStr) == 0:
        return False
    elif char == aStr[len(aStr)//2]:
        return True
    else:
        if char < aStr[len(aStr)//2]:
            return isIn(char,aStr[:len(aStr)//2])
        else:
            return isIn(char,aStr[1+len(aStr)//2:])
        