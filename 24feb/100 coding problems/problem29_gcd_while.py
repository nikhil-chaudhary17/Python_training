# Read two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Make numbers positive
a = abs(a)
b = abs(b)

# Find GCD using Euclidean algorithm
while b != 0:
    temp = b
    b = a % b
    a = temp

print("GCD:", a)