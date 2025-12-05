# Program that takes each score of the students and converts it to a grade

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

# For loop that loops through each student in the dictionary student_scores
for student in student_scores:
    # Assigns the value of student to a variable called score
    score = student_scores[student]
    
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectations"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)