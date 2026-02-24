def count_vowels(s):
    count = 0
    for ch in s:
        if ch in "aeiouAEIOU":
            count += 1
    return count

text = input("Enter a string: ")

print("Number of vowels:", count_vowels(text))

# Example:
# Enter a string: hello
# Number of vowels: 2