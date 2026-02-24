# Problem 96: Find first non-repeating character in string

s = input()

for ch in s:
    if s.count(ch) == 1:
        print(ch)
        break
else:
    print("No non-repeating character")

# Example Input:
# aabbcde

# Output:
# c