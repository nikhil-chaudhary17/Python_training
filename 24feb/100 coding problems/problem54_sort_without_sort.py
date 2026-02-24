numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# Bubble sort
for i in range(len(numbers)):
    for j in range(0, len(numbers) - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted list:", numbers)

# Example:
# Enter numbers separated by space: 5 2 8 1
# Sorted list: [1, 2, 5, 8]