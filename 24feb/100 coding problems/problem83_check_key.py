# Problem 83: Check whether key exists in dictionary

n = int(input())
d = {}

for _ in range(n):
    key, value = input().split()
    d[key] = int(value)

search_key = input()

if search_key in d:
    print("Key exists")
else:
    print("Key does not exist")

# Example Input:
# 2
# A 10
# B 20
# A

# Output:
# Key exists