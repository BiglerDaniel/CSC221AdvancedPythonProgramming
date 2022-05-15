#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Question 1:

In a previous assignment, we used a list to simulate a stack (Last In, First Out) 
data structure. Write a program that takes 5 string values from a user, adds 
them to a stack, and then pops them off the stack, printing them out in 
LIFO order.

Question 2:

Implement the same functionality as Question 1, but this time with a Stack class 
that uses Node objects to hold the internal structure of the stack.

Question 3:

In a previous assignment, we used a list to simulate a queue (First In, First Out) 
data structure. Write a program that takes 5 string values from a user, adds 
(enqueues) them to a queue , and then removes (dequeues) them from the queue, 
printing them out in FIFO order.

Question 4:

Implement the same functionality as Question 3, but this time with a Queue class 
that uses Node objects to hold the internal structure of the stack. You will find 
it much easier for this problem to use the TwoWayNode object since a queue adds 
to the tail and removes from the head.
"""
from stackNode import StackNode
from item import Item

class StackOrder:
    
    def __init__(self):
        
        start = Item("")
        xone = Item("")
        xtwo = Item("")
        xthree = Item("")
        xfour = Item("")
        xfive = Item("")
        
        self.items = [start, xone, xtwo, xthree, xfour, xfive]
        xoneNode = StackNode(xone)
        xtwoNode = StackNode(xtwo)
        xthreeNode = StackNode(xthree)
        xfourNode = StackNode(xfour)
        xfiveNode = StackNode(xfive)
        
        xoneNode.After = xtwoNode
        xtwoNode.After = xthreeNode
        xthreeNode.After = xfourNode
        xfourNode.After = xfiveNode
        
        xtwoNode.Previous = xoneNode
        xthreeNode.Previous = xtwoNode
        xfourNode.Previous = xthreeNode
        xfiveNode.Previous = xfourNode
        
        self.startNode = xoneNode
        

def option_menu():
    #first menu to show
    print("Please pick a menu option.")
    print("1. Last In, First Out / Stack.")
    print("2. LIFO, Stack class with Nodes.")
    print("3. First In, First Out / Queue.")
    print("4. FIFO, Queue class with Nodes.")
    print("Any other number. Exit.")

def stack():
    list = []
    text = ''
    print("Please enter 5 'strings' of text to be added, ")
    print("printed, and removed in Last In First Out order.")
    for x in range(5):
        print("This is input number" , x+1 ,": ")
        text = input()
        list.append(text)
    for x in range(5):
        print(x+1,": ", list[-1])
        list.pop(-1)
    
def stack_node():
    print("I would have done more for this part but I")
    print("still don't know what im doing, I only copied")
    print("some 'house.py' assignment stuff.")
    print("")

def queue():
    list = []
    text = ''
    print("Please enter 5 'strings' of text to be added, ")
    print("printed, and removed in First In First Out order.")
    for x in range(5):
        print("This is input number" , x+1 ,": ")
        text = input()
        list.append(text)
    for x in range(5):
        print(x+1,": ", list[0])
        list.pop(0)
    
def queue_node():
    print("Sorry, not done.")
    
def main():
    choice = int()
    again = "yes"
    
    print("Hello.")
    while again.lower() == "yes" or again.lower() == "y":
        option_menu()
        try:
            choice = int(input("Enter a number:"))
            if choice == 1:
                stack()
            elif choice == 2:
                stack_node()
            elif choice == 3:
                queue()
            elif choice == 4:
                queue_node()
            else:
                print("Bye.")
                again = "no"
        except:
            print("")
            print("ERROR")
            print("Please enter a NUMBER.")
main()