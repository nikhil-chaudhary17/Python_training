numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("Minimum value in tuple:", minimum)

# Example:
# Enter tuple elements separated by space: 10 25 5 40
# Minimum value in tuple: 5