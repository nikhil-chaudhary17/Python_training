# Read number
n = int(input("Enter a number: "))

if(n <= 0):
    print("Enter a positive number")
    exit()

armstrong_sum = 0
# Store original number
original = n

while n > 0:
    digit = n % 10
    armstrong_sum += digit * digit * digit
    n //= 10

# Check Armstrong condition
if armstrong_sum == original:
    print("Armstrong")
else:
    print("Not Armstrong")

#output
# Enter a number: 153
# Armstrong