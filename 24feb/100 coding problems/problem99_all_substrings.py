# Problem 99: Generate all substrings of a string

s = input()

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(s[i:j])

# Example Input:
# abc

# Output:
# a
# ab
# abc
# b
# bc
# c