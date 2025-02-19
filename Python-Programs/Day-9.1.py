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

Student_grades = {}

for student in Student_marks:
    marks = Student_marks[student]
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

print(Student_grades)
