# -*- coding: utf-8 -*-
"""
Daniel Bigler
biglerd7304
M1HW_BiglerDaniel
CSC-221-0001
"""

import random
def option_menu():
    #first menu to show
    print("Do you want easy or hard multiplication problems?")
    print("1. Easy (single digit)")
    print("2. Hard (double digits)")
    
def get_random_pair():
    """
    Generate two random one digit numbers,
    and return both of them at once
    """
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    
    return (num1, num2)

def get_random_pair_hard():
    """
    Generate two random one digit numbers,
    and return both of them at once
    """
    num1 = random.randint(0,99)
    num2 = random.randint(0,99)
    
    return (num1, num2)

def responces_for_answer_wrong():
    """
    Generate a number between 1 and 4
    for a "sorry, incorrect" message
    """
    wrongResponse = random.randint(1,4)
    if wrongResponse == 1:
        print("No. Please try again.")
    elif wrongResponse == 2:
        print("Wrong. Try once more.")
    elif wrongResponse == 3:
        print("Sorry, try again.")
    else:
        print("No. Keep trying.")

def responces_for_answer_right():
    """
    Generate a number between 1 and 4
    for a "You did it" message
    """
    rightResponse = random.randint(1,4)
    if rightResponse == 1:
        print("Very good!")
    elif rightResponse == 2:
        print("Nice work!")
    elif rightResponse == 3:
        print("Nice Job!")
    else:
        print("Keep up the good work!")
#ignore this comment area, it's a reminder
#def getUserAnswer():
#    while 
def main():
    difficultyLevel = int()
    num1 = int()
    num2 = int()
    answer = ''
    response = ''
    another = "Yes"
    yesOrNo = ''
    
    print("Hello.")
    option_menu()
    difficultyLevel = int(input("Enter a number option: "))
    
    while difficultyLevel != 1 and difficultyLevel != 2:
        option_menu()
        difficultyLevel = int(input("Enter a number option: "))
        
    while another.lower() == "yes" or another.lower() == "y":
        if difficultyLevel == 1:
            num1, num2 = get_random_pair()
        else:
            num1, num2 = get_random_pair_hard()
        answer = num1 * num2
        print("How much is ", num1, "times ", num2, "?")
        response = int(input())
        while response != answer:
            responces_for_answer_wrong()
            print("How much is ", num1, "times ", num2, "?")
            response = int(input())
        responces_for_answer_right()
        yesOrNo = input('Do you want another? ("Y/N"): ')
        while yesOrNo.lower() != "yes" and yesOrNo.lower() != "no" and \
        yesOrNo.lower() != "y" and yesOrNo.lower() != "n":
            yesOrNo = input('Do you want another? ("Y/N"): ')
        if yesOrNo.lower() == "no" or yesOrNo.lower() == "n":
            another = "no"
            print("Bye")
main()