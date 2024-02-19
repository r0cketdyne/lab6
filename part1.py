# Lab 6 - Part I
# Matthew Stephenson
# This program computes factorial for a value (N) entered by the user.
# STEP 1: Prompt the user for N and read it in and convert it into an integer\
var_fact = float(input("Throw me an integer...we're going to add bang and compute the resulting factorial"))
var_sum = 1
# STEP 2: Initialize factorial to a default value before multiplying

# values into it
# STEP 3: Complete the following loop to compute factorial

while var_fact > 0 : # STEP 3a: what is the condition to keep going?

    # STEP 3b: multiply N x factorial and save it back into factorial variable
     var_sum *= var_fact
     var_fact -=1
    # STEP 3c: decrement N by 1
    

# Step 4: Print out The resulting factorial value
#this is kind of mathy ngl
print(var_sum)