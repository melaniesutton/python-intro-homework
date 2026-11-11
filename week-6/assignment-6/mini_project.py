numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93,
           31, 66, 14, 47, 78, 3, 59, 22, 86, 40]


# Find minimum
def find_min(numbers):
    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest


# Find maximum
def find_max(numbers):
    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest


# Linear search
def search(numbers, target):
    for i in range(len(numbers)):
        if numbers[i] == target:
            return i

    return -1


# Bubble sort
def bubble_sort(numbers):
    sorted_numbers = numbers.copy()

    swapped = True

    while swapped:
        swapped = False

        for i in range(len(sorted_numbers) - 1):
            if sorted_numbers[i] > sorted_numbers[i + 1]:

                sorted_numbers[i], sorted_numbers[i + 1] = (
                    sorted_numbers[i + 1],
                    sorted_numbers[i]
                )

                swapped = True

    return sorted_numbers


# Display menu and get user's choice
def show_menu():
    print("\n=== Number Cruncher ===")
    print("1. Find minimum")
    print("2. Find maximum")
    print("3. Search for a number")
    print("4. Sort the list")
    print("5. Quit")

    choice = input("Choose an option (1-5): ")

    return choice


# Main function
def main():

    while True:

        choice = show_menu()

        # Find minimum
        if choice == "1":
            result = find_min(numbers)
            print("Minimum number:", result)

        # Find maximum
        elif choice == "2":
            result = find_max(numbers)
            print("Maximum number:", result)

        # Linear search
        elif choice == "3":
            search_num = int(input("Enter a number to search: "))

            index = search(numbers, search_num)

            if index != -1:
                print(f"Found {search_num} at index {index}.")
            else:
                print(f"{search_num} was not found in the list.")

        # Bubble sort
        elif choice == "4":
            sorted_numbers = bubble_sort(numbers)
            print("Original list:", numbers)
            print("Sorted list:", sorted_numbers)

        # Quit
        elif choice == "5":
            print("Goodbye! Thanks for using Number Cruncher.")
            return

        else:
            print("Invalid option. Please choose between 1 and 5.")


if __name__ == "__main__":
    main()