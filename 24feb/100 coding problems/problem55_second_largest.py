numbers = list(map(int, input("Enter numbers separated by space: ").split()))

largest = second = -999999

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

print("Second largest number is:", second)

# Example:
# Enter numbers separated by space: 10 20 5 40
# Second largest number is: 20