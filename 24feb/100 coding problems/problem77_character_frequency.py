text = input("Enter a string: ")

frequency = {}

for ch in text:
    if ch in frequency:
        frequency[ch] += 1
    else:
        frequency[ch] = 1

print("Character frequency:", frequency)

# Example:
# Enter a string: hello
# Character frequency: {'h':1, 'e':1, 'l':2, 'o':1}