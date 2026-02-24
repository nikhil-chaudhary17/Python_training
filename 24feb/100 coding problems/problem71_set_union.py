set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

union_set = set1.union(set2)

print("Union of sets:", union_set)

# Example:
# Enter first set elements separated by space: 1 2 3
# Enter second set elements separated by space: 3 4 5
# Union of sets: {1, 2, 3, 4, 5}