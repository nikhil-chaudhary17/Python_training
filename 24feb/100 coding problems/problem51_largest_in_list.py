# Input
numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest element is:", largest)

# Example:
# Enter numbers separated by space: 10 25 5 40
# Largest element is: 40