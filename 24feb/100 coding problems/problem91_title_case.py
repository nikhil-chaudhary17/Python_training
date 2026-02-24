# Problem 91: Convert string to title case manually

s = input()

result = ""
new_word = True

for ch in s:
    if ch == " ":
        result += ch
        new_word = True
    else:
        if new_word:
            result += ch.upper()
            new_word = False
        else:
            result += ch.lower()

print(result)

# Example Input:
# hello world python

# Output:
# Hello World Python