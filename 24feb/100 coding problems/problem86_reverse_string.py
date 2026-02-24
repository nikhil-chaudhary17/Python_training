# Problem 86: Reverse a string without slicing

s = input()

reversed_string = ""

for char in s:
    reversed_string = char + reversed_string

print(reversed_string)

# Example Input:
# hello

# Output:
# olleh