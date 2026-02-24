def is_palindrome(s):
    return s == s[::-1]

text = input("Enter a string: ")

if is_palindrome(text):
    print("It is a Palindrome")
else:
    print("It is not a Palindrome")

# Example:
# Enter a string: madam
# It is a Palindrome