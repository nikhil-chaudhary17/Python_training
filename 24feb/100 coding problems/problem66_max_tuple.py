numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

maximum = numbers[0]

for num in numbers:
    if num > maximum:
        maximum = num

print("Maximum value in tuple:", maximum)

# Example:
# Enter tuple elements separated by space: 10 25 5 40
# Maximum value in tuple: 40