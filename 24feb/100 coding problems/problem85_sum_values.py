# Problem 85: Find sum of all dictionary values

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

total = sum(d.values())

print(total)

# Example Input:
# 3
# A 10
# B 20
# C 30

# Output:
# 60