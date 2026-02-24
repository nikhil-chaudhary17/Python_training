set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

difference_set = set1.difference(set2)

print("Difference of sets (Set1 - Set2):", difference_set)

# Example:
# Difference of sets (Set1 - Set2): {1, 2}