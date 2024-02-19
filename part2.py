# Lab6 - Part II
# Matthew Stephenson
# This program reads in numbers until the user enters a 0. For each number
# entered, prints whether it is even or odd.

def is_even(number):
    return number % 2 == 0
#we are going to define some funcs...yay! sadly they are not built in. this is for even
def is_odd(number):
    return number % 2 != 0
#the function definition above sadly isnt inluded in the math lib. so we made it here

number = int(input("Enter a number. I will tell you if it is odd or even: "))

while number != 0:
    if is_even(number):
        print(f"The number {number} is even.")
    elif is_odd(number):
        print(f"The number {number} is odd.")
    
    # Prompt the user for the next number inside the loop
    number = int(input("Please enter another number, 0 to stop: "))

print("\nYou entered 0. Goodbye")
