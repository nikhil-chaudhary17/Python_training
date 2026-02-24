# Read a character
ch = input("Enter a character: ")

# Check if digit
if ch.isdigit():
    print("Digit")

# Check if alphabet
elif ch.isalpha():
    print("Alphabet")

# If neither    
else:
    print("Special Character")