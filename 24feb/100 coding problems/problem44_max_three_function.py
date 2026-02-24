def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print("Maximum number is:", find_max(a, b, c))

# Example:
# Enter first number: 10
# Enter second number: 25
# Enter third number: 15
# Maximum number is: 25
