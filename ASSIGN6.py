# Ask the user to enter each grade (use a counter to control the loop).
# Add each grade to a list as you loop.
# Then compute the average.

count = 0
grades = []  # Use a list to store the grades

# Initialize a counter to zero
while count < 5:
    # Convert the input to float and append it to the grades list
    grade = float(input(f"Enter the final grade for student {count + 1}: "))
    grades.append(grade)
    count += 1

# Calculate the sum and average
arr_sum = sum(grades)
average = arr_sum / len(grades)

print("Grades:", grades)
print("Average:", average)
#I basically coded this from scratch given the problem statement for lecture 6 or 
#whatever