# Read number
n = int(input("Enter a number: "))

reverse = 0

# Handle negative numbers
sign = 1
if n < 0:
    sign = -1
    n = abs(n) # Make n positive for reversal

# Reverse number using while loop
while n > 0:
    digit = n % 10
    reverse = reverse * 10 + digit
    n = n // 10

print(sign * reverse)

#output
# Enter a number: -1234
# -4321