list1 = list(map(int, input("Enter first list elements: ").split()))
list2 = list(map(int, input("Enter second list elements: ").split()))

common = []

for num in list1:
    if num in list2 and num not in common:
        common.append(num)

print("Common elements:", common)

# Example:
# Enter first list elements: 1 2 3 4
# Enter second list elements: 3 4 5 6
# Common elements: [3, 4]