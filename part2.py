#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 14:37:56 2024

@author: stephenson
"""

#we are going to define some funcs...yay! sadly they are not built in

# Lab6 - Part II
#Matthew Stephenson
# This program reads in numbers until the user enters a 0. For each number
# entered, prints whether it is even or odd.

def is_even(number):
    return number % 2 == 0
#we are going to define some funcs...yay! sadly they are not built in. this is for even
def is_odd(number):
    return number % 2 != 0
#the function definition above sadly isnt inluded in the math lib. so we made it here

number = int(input("Enter a number. I will tell you if it is odd or even: "))
while number != 0: # STEP 1: condition that allows the loop to continue
# STEP 2: print out whether the number is odd or even
    if is_even(number):
        print("the number is even")

    elif is_odd(number):
        print("the number is odd")
# STEP 3: prompt the user for the next number
print("\nYou entered 0. Goodbye")

"""
Finishing Up:
Upload both of your program files for this lab submission. (It is permissible to put them both into the
same program file if you wish.)
Enter a number. I will tell you if it is odd or even: 8
The number 8 is even.
Please enter another number, 0 to stop: 187
The number 187 is odd.
Please enter another number, 0 to stop: -17
The number -17 is odd.
Please enter another number, 0 to stop: 0
You entered 0. Goodbye
"""

#yay everything is local going to get food and come back slightly later. exam prep after this yay