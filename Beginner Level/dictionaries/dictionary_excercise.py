student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}
for key in student_scores:
    criteria = ""
    current_score = student_scores[key]
    if current_score in range (91, 100):
        criteria = "Outstanding"
    if current_score in range (81, 90):
        criteria = "Exceeds Expectations"
    if current_score in range (71, 80):
        criteria = "Acceptable"
    if current_score <= 70:
        criteria = "Fail"
    student_grades[key] = criteria
    
for key, value in student_grades.items():
    print(f"{key} : {value}")