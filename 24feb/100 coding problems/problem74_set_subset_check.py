set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

if set1.issubset(set2):
    print("Set1 is subset of Set2")
else:
    print("Set1 is not subset of Set2")

# Example:
# Set1 is subset of Set2