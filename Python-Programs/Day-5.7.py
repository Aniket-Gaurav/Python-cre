# The code below takes a list of numbers as input, converts them to integers,
# and finds the maximum number in the list.

numbers = input("Enter list of numbers: ")  # Prompt the user to enter a list of numbers
number = numbers.split()  # Split the input string into a list of strings

count = 0  # Initialize a counter variable to keep track of the number of elements in the list
for i in number:  # Iterate over each element in the list
    count += 1  # Increment the counter for each element

# Convert each element in the list to an integer
for i in range(count):
    number[i] = int(number[i])

# Initialize the maximum number variable with the first element of the list
maximum_number = number[0]

# Iterate over each element in the list and update the maximum number if necessary
for i in number:
    if i > maximum_number:
        maximum_number = i

# Print the maximum number
print(f"The maximum number is: {maximum_number}")<<<<<<< Tabnine <<<<<<<
numbers = input("Enter list of numbers: ")#-
number = numbers.split()#-
# The code below takes a list of numbers as input, converts them to integers,#+
# and finds the maximum number in the list.#+

count =0#-
for i in number:#-
    count +=1#-
numbers = input("Enter list of numbers: ")  # Prompt the user to enter a list of numbers#+
number = numbers.split()  # Split the input string into a list of strings#+

count = 0  # Initialize a counter variable to keep track of the number of elements in the list#+
for i in number:  # Iterate over each element in the list#+
    count += 1  # Increment the counter for each element#+
#+
# Convert each element in the list to an integer#+
for i in range(count):
    number[i] = int(number[i])

# Initialize the maximum number variable with the first element of the list#+
maximum_number = number[0]
#+
# Iterate over each element in the list and update the maximum number if necessary#+
for i in number:
    if i > maximum_number:
        maximum_number = i
#+
# Print the maximum number#+
print(f"The maximum number is: {maximum_number}")