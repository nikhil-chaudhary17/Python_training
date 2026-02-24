# Read number
n = int(input("Enter a number n: "))

total = 0

# Sum of first n natural numbers
for i in range(1, n + 1):
    total = total + i

print(total)
#output
# Enter a number n: 5
# 15