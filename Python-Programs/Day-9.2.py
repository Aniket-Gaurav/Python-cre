# Student_data is a dictionary that stores student data
Student_data = [
    {"Name": "Ram", "roll_no": 1, "marks": 85, "grade": "A+"},  # Ram's data
    {"Name": "Mohan", "roll_no": 15, "marks": 77, "grade": "A+"},  # Mohan's data
]

# Print Ram's data
print(Student_data[0]) # Print Ram's data

# Print Mohan's roll number
print(Student_data[1]["roll_no"]) # Print Mohan's roll number

# Add a phone number to Ram's data
Student_data[0]["phone_no"] = 9079797
print(Student_data[0]) # Add a phone number to Ram's data

# Delete Ram's phone number
del Student_data[0]["phone_no"]
print(Student_data[0]) # Delete Ram's phone number


# <-------------------------------------------------------------------------------->

# travel_data is a dictionary that stores travel data
travel_data = {
    "Gujrat": ["Dwarkadhis", "Somnath", "Statue of Unity"],  # Gujarat travel data
    "Maharashtra": ["Pune", "Mumbai", "Nashik"],  # Maharashtra travel data
    "Rajasthan": ["Jaipur", "Udaipur", "Ajmer"],  # Rajasthan travel data
}
print(travel_data) # Print travel data
print(travel_data["Gujrat"][2]) # Print Statue of Unity from Gujarat travel data


# <-------------------------------------------------------------------------------->

# Student_data is a list of dictionaries that stores student data
Student_data = [
    {"Name": "Ram", "roll_no": 1, "marks": 85, "grade": "A+"},  # Ram's data
    {"Name": "Mohan", "roll_no": 15, "marks": 77, "grade": "A+"},  # Mohan's data
]

# Print Ram's name
print(Student_data[0]["Name"]) # Print Ram's name

# Print Mohan's roll number
print(Student_data[1]["roll_no"]) # Print Mohan's roll number

# Function to add a new student
def add_new_student(name, roll_no, marks, grade):
    new_student = {}
    new_student["Name"] = name
    new_student["roll_no"] = roll_no
    new_student["marks"] = marks
    new_student["grade"] = grade
    Student_data.append(new_student)

add_new_student("Shyam", 22, 18, "A+") # Add a new student

print(Student_data) # Print Student_data

