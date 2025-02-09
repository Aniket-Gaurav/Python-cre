# Get user input for heights, separated by commas
heights = input("Enter all the heights separated by comma: ")

# Split the input string into a list of heights
height_list = heights.split(",")

# Initialize a counter to keep track of the number of heights
count = 0

# Count the number of heights in the list
for height in height_list:
    count += 1

# Convert each height in the list from string to integer
for i in range(count):
    height_list[i] = int(height_list[i])

# Initialize a variable to store the sum of heights
sum = 0

# Calculate the sum of all heights
for height in height_list:
    sum += height

# Print the average height
print(f"The average height is: {sum/count}")