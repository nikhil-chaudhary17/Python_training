numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for num in numbers:
    total += num

print("Sum of elements:", total)

# Example:
# Enter numbers separated by space: 1 2 3 4
# Sum of elements: 10