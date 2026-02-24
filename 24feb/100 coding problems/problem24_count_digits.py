# Read number
n = int(input("Enter a number: "))

# Make number positive
n = abs(n)

count = 0

# Special case if number is 0
if n == 0:
    count = 1
else:
    # Count digits using while loop
    while n > 0:
        n = n // 10
        count += 1

print(count) 

#output
# Enter a number: -1234 
# 4