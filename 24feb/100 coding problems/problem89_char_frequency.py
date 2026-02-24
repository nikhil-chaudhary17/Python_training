# Problem 89: Find frequency of each character in string

s = input()

freq = {}

for char in s:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

print(freq)

# Example Input:
# hello

# Output:
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}