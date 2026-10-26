student = {"name": "John", "grade": "B", "subjects": ["math", "history", "art", "english"]}
for key, value in student.items():
    print(f"{key}: {value}")

student["graduated"] = "False"
print(student)
