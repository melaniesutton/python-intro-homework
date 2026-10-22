score = int(input("What is your score? "))

if score >= 90:             # 90 or greater
    print("Grade: A")
elif score >= 80:           # 80-89 
    print("Grade: B")
elif score >= 70:           # 70-79
    print("Grade: C")       
elif score >= 60:           # 60-69
    print("Grade: D")
else:                       # 59 or below
    print("Grade: F")