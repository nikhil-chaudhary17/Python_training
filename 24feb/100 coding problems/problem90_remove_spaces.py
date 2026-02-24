# Problem 90: Remove spaces from string

s = input()

result = ""

for char in s:
    if char != " ":
        result += char

print(result)

# Example Input:
# Hello World

# Output:
# HelloWorld