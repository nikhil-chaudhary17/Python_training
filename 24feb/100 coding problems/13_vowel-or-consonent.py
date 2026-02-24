# Read a character
ch = input("Enter a character: ")

# Convert to lowercase to handle both upper and lower case
ch = ch.lower()

# Check if character is alphabet first
if ch.isalpha():
    # Check vowel condition
    if ch in ['a', 'e', 'i', 'o', 'u']:
        print("Vowel")
    else:
        print("Consonant")
else:
    print("Not an alphabet")

# output
# Enter a character: A
# Vowel