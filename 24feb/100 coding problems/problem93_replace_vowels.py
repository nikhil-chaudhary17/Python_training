# Problem 93: Replace all vowels with *

s = input()
vowels = "aeiouAEIOU"
result = ""

for ch in s:
    if ch in vowels:
        result += "*"
    else:
        result += ch

print(result)

# Example Input:
# hello world

# Output:
# h*ll* w*rld