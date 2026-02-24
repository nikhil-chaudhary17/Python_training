def unique_elements(lst):
    unique = []
    for item in lst:
        if item not in unique:
            unique.append(item)
    return unique

numbers = list(map(int, input("Enter numbers separated by space: ").split()))

print("Unique elements:", unique_elements(numbers))

# Example:
# Enter numbers separated by space: 1 2 2 3 4 4
# Unique elements: [1, 2, 3, 4]