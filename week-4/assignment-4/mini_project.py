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

for student in students:
    print(f"{student['name']}: {student['score']}")

# Find the top scorer
highest_score = 0 
highest_scoring_student = "name"

for student in students:
    score = student["score"]

    if score > highest_score:
        highest_score = score
        highest_scoring_student = student["name"]

print(f"Top scorer: {highest_scoring_student} ({highest_score})")

# Class average: 81.25
total = 0
for student in students:
    total += student["score"]
average = total / len(students)
print(f"Class average: {average}")  

# Print subjects offered
unique_subjects = set()
for student in students:
    unique_subjects.add(student["subject"])
print(f"Subjects offered: {unique_subjects}")

# High scorers: ["Jazmine", "Sara", "Priya", "Mia", "Eli"]
high_scorers = []
for student in students:
    if student["score"] > 75:
        high_scorers.append(student["name"])
print(high_scorers)   
