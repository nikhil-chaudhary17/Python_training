# Read string
s = input("Enter a string: ")

count = 0

# Count vowels
for ch in s:
    if ch in "aeiouAEIOU":
        count = count + 1

print(count)

#output
# Enter a string: Hello World