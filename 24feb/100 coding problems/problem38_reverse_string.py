# Read string
s = input("Enter a string: ")

reverse = ""

# Reverse string using for loop
for i in range(len(s) - 1, -1, -1):
    reverse = reverse + s[i]

print(" Reversed string is:", reverse)

# Example Input:
# hello
# Example Output:
# olleh