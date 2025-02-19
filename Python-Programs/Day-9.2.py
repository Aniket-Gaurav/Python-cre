# Student_data is a dictionary that stores student data
Student_data = [
    {"Name": "Ram", "roll_no": 1, "marks": 85, "grade": "A+"},  # Ram's data
    {"Name": "Mohan", "roll_no": 15, "marks": 77, "grade": "A+"},  # Mohan's data
]

# Print Ram's data
print(Student_data[0])

# Print Mohan's roll number
print(Student_data[1]["roll_no"])
# Add a phone number to Ram's data
Student_data[0]["phone_no"] = 9079797
print(Student_data[0])

# Delete Ram's phone number
del Student_data[0]["phone_no"]
print(Student_data[0])


# <-------------------------------------------------------------------------------->

# travel_data is a dictionary that stores travel data
travel_data = {
    "Gujrat": ["Dwarkadhis", "Somnath", "Statu of Unity"],  # Gujarat travel data
    "Maharashtra": ["Pune", "Mumbai", "Nashik"],  # Maharashtra travel data
    "Rajasthan": ["Jaipur", "Udaipur", "Ajmer"],  # Rajasthan travel data
}
print(travel_data)
print(travel_data["Gujrat"][2])  # Print Statue of Unity from Gujarat travel data


# <-------------------------------------------------------------------------------->

# Student_data is a list of dictionaries that stores student data
Student_data = [
    {"Name": "Ram", "roll_no": 1, "marks": 85, "grade": "A+"},  # Ram's data
    {"Name": "Mohan", "roll_no": 15, "marks": 77, "grade": "A+"},  # Mohan's data
]

# Print Ram's name
print(Student_data[0]["Name"])

# Print Mohan's roll number
print(Student_data[1]["roll_no"])
