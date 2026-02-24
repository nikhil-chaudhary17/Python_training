numbers = list(map(int, input("Enter numbers separated by space: ").split()))

if numbers == numbers[::-1]:
    print("List is Palindrome")
else:
    print("List is not Palindrome")

# Example:
# Enter numbers separated by space: 1 2 3 2 1
# List is Palindrome