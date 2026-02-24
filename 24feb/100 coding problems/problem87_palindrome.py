# Problem 87: Check whether string is palindrome

s = input()

reversed_string = ""

for char in s:
    reversed_string = char + reversed_string

if s == reversed_string:
    print("Palindrome")
else:
    print("Not Palindrome")

# Example Input:
# madam

# Output:
# Palindrome