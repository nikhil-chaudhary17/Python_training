# Problem 97: Count uppercase and lowercase letters

s = input()

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase:", upper)
print("Lowercase:", lower)

# Example Input:
# Hello World

# Output:
# Uppercase: 2
# Lowercase: 8