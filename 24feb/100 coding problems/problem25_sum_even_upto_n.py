# Read value of N
n = int(input("Enter a number N: "))

i = 1
total = 0

# Find sum of even numbers up to N
while i <= n:
    if i % 2 == 0:
        total += i
    i += 1

print(total)

#output
# Enter a number N: 10
# 30