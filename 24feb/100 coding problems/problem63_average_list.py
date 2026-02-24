numbers = list(map(int, input("Enter numbers separated by space: ").split()))

total = 0
for num in numbers:
    total += num

average = total / len(numbers)

print("Average is:", average)

# Example:
# Enter numbers separated by space: 2 4 6 8
# Average is: 5.0