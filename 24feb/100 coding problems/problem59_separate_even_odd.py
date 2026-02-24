numbers = list(map(int, input("Enter numbers separated by space: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even numbers:", even)
print("Odd numbers:", odd)

# Example:
# Enter numbers separated by space: 1 2 3 4 5
# Even numbers: [2, 4]
# Odd numbers: [1, 3, 5]