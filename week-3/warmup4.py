number = int(input("Enter a number: "))

if number == 0:
    print(f"{number} is zero. ")
    print(f"{number} is even. ")
elif number > 0 and number % 2 == 0:
    print(f"{number} is positive. ")
    print(f"{number} is even")
elif number < 0 and number % 2 == 0:
    print(f"{number} is negative. ")
    print(f"{number} is even. ")
elif number < 0 and number % 3 == 0:
    print(f"{number} is negative. ")
    print(f"{number} is odd. ")
else:
    print(f"{number} is odd. ")
    print(f"{number} is positive. ")