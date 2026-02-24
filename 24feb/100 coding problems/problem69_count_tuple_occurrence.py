numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))
element = int(input("Enter element to count: "))

count = 0
for num in numbers:
    if num == element:
        count += 1

print("Element appears", count, "times")

# Example:
# Enter tuple elements separated by space: 1 2 2 3
# Enter element to count: 2
# Element appears 2 times