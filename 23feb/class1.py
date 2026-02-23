# Create list of 20 numbers
numbers = [int(input(f"Enter number {i+1}: ")) for i in range(10)]

print("Original List:", numbers)

target = int(input("Enter number to delete (keep first occurrence): "))

if target in numbers:
    first = numbers.index(target)

     # Remove all occurrences
    numbers = [num for num in numbers if num != target]

     # Reinsert the first occurrence
    numbers.insert(first, target)

    print("Updated List:", numbers)
else:
    print("Number not found in the list.")