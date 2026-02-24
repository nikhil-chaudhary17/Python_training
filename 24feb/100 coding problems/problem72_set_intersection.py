set1 = set(map(int, input("Enter first set elements separated by space: ").split()))
set2 = set(map(int, input("Enter second set elements separated by space: ").split()))

intersection_set = set1.intersection(set2)

print("Intersection of sets:", intersection_set)

# Example:
# Intersection of sets: {3}