numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

while True: 
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    # Find minimum
    if choice == "1":
        smallest = numbers[0]

        for num in numbers:
            if num < smallest:
                smallest = num

        print("Minimun number:", smallest)

    # Find maximum
    elif choice == "2":
        largest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num
        
        print("Maximum number:", largest)

    # Linear search
    elif choice == "3":
        search_num = int(input("Enter a number to search: "))

        found = False
        index = -1 

        for i in range(len(numbers)):
            if numbers[i] == search_num:
                print(f"Found {search_num} at index {i}.")
                found = True
                index = i
                break

        if not found:
            print(f"{search_num} was not found in the list.")

    # Bubble sort
    elif choice == "4":
        swapped = True

        while swapped:
            swapped = False 

            for i in range (len(numbers) - 1):
                if numbers[i] > numbers[i + 1]:
                    # Swap adjacent elements
                    numbers[i], numbers[i + 1] = numbers [i + 1], numbers[i]
                    swapped = True

        print("Sorted list:", numbers)

    # Quit
    elif choice == "5":
        print("Goodbye! Thanks for using Number Cruncher.")
        break

    else:
        print("Invaild option. Please choose between 1 and 5.")

