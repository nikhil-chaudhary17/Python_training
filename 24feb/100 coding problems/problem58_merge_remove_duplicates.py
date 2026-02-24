list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

merged = list1 + list2
unique = []

for num in merged:
    if num not in unique:
        unique.append(num)

print("Merged list without duplicates:", unique)

# Example:
# Enter first list elements: 1 2 3
# Enter second list elements: 2 3 4
# Merged list without duplicates: [1, 2, 3, 4]