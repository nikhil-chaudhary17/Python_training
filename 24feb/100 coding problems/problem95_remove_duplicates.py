# Problem 95: Remove duplicate characters from string

s = input()
result = ""

for ch in s:
    if ch not in result:
        result += ch

print(result)

# Example Input:
# programming

# Output:
# progamin