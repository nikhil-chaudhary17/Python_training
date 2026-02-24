# Read number
n = int(input("Enter a number: "))

# Initialize factorial result
fact = 1
i = 1

# Calculate factorial using while loop
while i <= n:
    fact *= i
    i += 1   # Increment counter

print(fact)

#output
# Enter a number: 5
# 120