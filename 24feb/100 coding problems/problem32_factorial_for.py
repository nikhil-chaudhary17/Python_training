# Read number
n = int(input("Enter a number: "))

fact = 1

# Calculate factorial using for loop
for i in range(1, n + 1):
    fact = fact * i

print(" Factorial of", n, "is", fact)