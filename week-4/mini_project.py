students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

# Top scorer: Priya (95)
for student in students:
    print(f"{student['name']}: {student['score']}")

# Class average: 81.25
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")  

# Subjects offered: {"Python", "Data', "Web"}
tags = {"Python", "Data", "Web"}
for tag in tags:
    print(tag)

# High scorers: ["Jazmine", "Sara", "Priya", "Mia", "Eli"]
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])
print(high_scorers)   
