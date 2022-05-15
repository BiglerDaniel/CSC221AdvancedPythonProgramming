#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Daniel Bigler
biglerd7304
M2HW_Bigler
CSC-221-0001
"""
import random

def option_menu():
    #first menu to show
    print("Please pick a menu option.")
    print("1. Guess the Number.")
    print("2. Functions Returning Tuples.")
    print("3. Simulating a Queue with a List.")
    print("Any other number. Exit.")
    
def game():
    hiddenNum = int()
    guess = int()
    again = "yes"
    yesOrNo = ''
    list = []
    length = int()
        
    while again.lower() == "yes" or again.lower() == "y":
        hiddenNum = random.randint(1,1000)
        print("Guess The Number Between 1 And 1000")
        print("With The Fewest Guesses!")
        while hiddenNum != guess:
            try:
                guess = int(input("Enter a number: "))
                if guess > hiddenNum:
                    print("Too high. Try again.")
                elif guess < hiddenNum:
                    print("Too low. Try again.")
                else:
                    print("Congratulations. You guessed the number!",\
                          hiddenNum)
                list.append(guess)
            except:
                print("Please only integers!")
        print(list)
        length = len(list)
        if length < 11:
            print("Either you know the secret or you got lucky!")
        elif length >= 11:
            print("You should be able to do better!")
        yesOrNo = input('Do you want to play again? ("Y/N"): ')
        
        while yesOrNo.lower() != "yes" and yesOrNo.lower() != "no" and \
        yesOrNo.lower() != "y" and yesOrNo.lower() != "n":
            yesOrNo = input('Do you want to play again? ("Y/N"): ')
        if yesOrNo.lower() == "no" or yesOrNo.lower() == "n":
            again = "no"
            print("")
        list.clear()


def rotate(a, b, c):
    """
    p.202
    rotate a tuple
    =====================================
    input: three values
    output: tuple, with the order rotated
    
    example
    >rotate(1, 2, 3)
    (2, 3, 1)
    >rotate("a", "b", "c")
    ("b", "c", "a")
    """
    a, b, c = (b, c, a)
    print(f'a = {a}; b = {b}; c = {c}')
    return (a,b,c)
def spin():
    a = "Doug"
    b = "22"
    c = "1984"
    
    print("a =",a,"b =",b,"c =",c)
    print("Rotate three times and...")
    a,b,c = rotate(a, b, c)
    a,b,c = rotate(a, b, c)
    rotate(a, b, c)
    print("")
def queue():
    print("")
    print("")
    list = []
    print("Enqueue '3' at end.")
    list.append(3)
    print(list)
    print("")
    print("Enqueue '2' at the end.")
    list.append(2)
    print(list)
    print("")
    print("Enqueue  '1' at the end.")
    list.append(1)
    print(list)
    print("")
    print("Dequeue '3' from the beginning.")
    list.pop(0)
    print(list)
    print("")
    print("Dequeue '2' from the beginning.")
    list.pop(0)
    print(list)
    print("")
    print("Dequeue '1' from the beginning.")
    list.pop(0)
    print(list)
    print("")
def main():
    choice = int()
    again = "yes"
    
    print("Hello.")
    while again.lower() == "yes" or again.lower() == "y":
        option_menu()
        try:
            choice = int(input("Enter a number:"))
            if choice == 1:
                game()
            elif choice == 2:
                spin()
            elif choice == 3:
                queue()
            else:
                print("Bye.")
                again = "no"
        except:
            print("")
            print("")
            print("Please enter a NUMBER.")
main()
