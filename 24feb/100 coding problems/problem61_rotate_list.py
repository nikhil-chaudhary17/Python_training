numbers = list(map(int, input("Enter numbers separated by space: ").split()))
k = int(input("Enter number of positions to rotate: "))

k = k % len(numbers)

rotated = numbers[k:] + numbers[:k]

print("Rotated list:", rotated)

# Example:
# Enter numbers separated by space: 1 2 3 4 5
# Enter number of positions to rotate: 2
# Rotated list: [3, 4, 5, 1, 2]