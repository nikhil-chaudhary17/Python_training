numbers = tuple(map(int, input("Enter tuple elements separated by space: ").split()))

unique = True

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            unique = False
            break

if unique:
    print("All elements are unique")
else:
    print("Tuple contains duplicate elements")

# Example:
# Enter tuple elements separated by space: 1 2 3 4
# All elements are unique