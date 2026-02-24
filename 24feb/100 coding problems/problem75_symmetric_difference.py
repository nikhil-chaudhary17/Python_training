set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

sym_diff = set1.symmetric_difference(set2)

print("Symmetric difference:", sym_diff)

# Example:
# Symmetric difference: {1, 2, 4, 5}