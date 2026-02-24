# Problem 81: Find key with maximum value

# Input:
# First line → number of key-value pairs
# Next n lines → key value

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

# Find key with maximum value
max_key = max(d, key=d.get)

print(max_key)

# Example Input:
# 3
# A 50
# B 80
# C 60

# Output:
# B