# Problem 84: Create dictionary from two lists

keys = input().split()
values = list(map(int, input().split()))

d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)

# Example Input:
# A B C
# 10 20 30

# Output:
# {'A': 10, 'B': 20, 'C': 30}