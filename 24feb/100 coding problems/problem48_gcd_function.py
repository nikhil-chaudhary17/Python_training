def find_gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD is:", find_gcd(a, b))

# Example:
# Enter first number: 12
# Enter second number: 18
# GCD is: 6