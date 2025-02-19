# dictionary with student names as keys and marks as values
Student_marks = {
    "John": 85,
    "Jane": 92,
    "Alice": 78,
    "Bob": 88,
    "Diana": 90,
    "Eve": 80,
    "Frank": 75,
    "Grace": 95,
    "Henry": 82,
    "Ivy": 93,
}

# an empty dictionary to store the student grades
Student_grades = {}

# iterate through each student in the Student_marks dictionary
for student in Student_marks:
    # get the marks for each student
    marks = Student_marks[student]
    # assign a grade to each student based on their marks
    if marks >= 90:
        Student_grades[student] = "A+"
    elif marks >= 80:
        Student_grades[student] = "A"
    elif marks >= 70:
        Student_grades[student] = "B"
    elif marks >= 60:
        Student_grades[student] = "C"
    elif marks >= 50:
        Student_grades[student] = "D"
    else:
        Student_grades[student] = "F"

# print the Student_grades dictionary
print(Student_grades)

