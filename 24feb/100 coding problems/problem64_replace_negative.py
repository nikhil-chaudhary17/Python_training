numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0

print("Updated list:", numbers)

# Example:
# Enter numbers separated by space: 1 -2 3 -4
# Updated list: [1, 0, 3, 0]