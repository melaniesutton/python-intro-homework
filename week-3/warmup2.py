age = int(input("Enter your age: "))

if age <= 12:                       # Ages 12 and under
    print("You are a Child.")
elif age <= 17:                     # Ages 13-17
    print("You are a Teen.")
elif age <= 64:                     # Ages 18-64
    print("You are an Adult.")
else:                               # Ages 65 and up
    print("You are a Senior.")