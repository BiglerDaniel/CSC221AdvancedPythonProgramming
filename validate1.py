# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def getNumberFromUser():
    """
    user will enter a validated number
    input: none
    output: a valid number
    we need to do two things:
        1. don't crash
        2. loop until valid input
    """
    # Loop with a flag
    print("Please enter a number:")
    validInput = False
    while validInput == False:
        print("Please enter a number:")
        try:
            userText = input()
            num = int(userText)
            # following line never called
            # if an exception occurs
            validInput = True
        except:
            print('"', userText, '" is not a valid number.')
        
        
    return num

def getPositiveNumberFromUser():
    """
    user will enter a validated number
    input: none
    output: a valid number
    we need to do two things:
        1. don't crash
        2. loop until valid input greater than zero
    """
    # Loop with a flag
    validInput = False
    while validInput == False:
        print("Enter a positive number")
        num = int(input())
        if num > 0:
            validInput = True
        else:
            print("Please input a positive number.")
            
    return num


def main():
    """ test user input with addition """
    #print("Enter a number:")
    num1 = getPositiveNumberFromUser()
    
    #print("Enter another number:")
    num2 = getPositiveNumberFromUser()
    
    print("The sum is :",num1+num2)
    
    
main()
