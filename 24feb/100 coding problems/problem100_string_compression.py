# Problem 100: Compress a string using character counts

s = input()

result = ""
count = 1

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        result += s[i - 1] + str(count)
        count = 1

# Add last character
result += s[-1] + str(count)

print(result)

# Example Input:
# aaabbc

# Output:
# a3b2c1