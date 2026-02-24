numbers = list(map(int, input("Enter numbers separated by space: ").split()))

smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element is:", smallest)

# Example:
# Enter numbers separated by space: 10 25 5 40
# Smallest element is: 5