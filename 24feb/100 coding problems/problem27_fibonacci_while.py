# Read number of terms
n = int(input("Enter the number of terms: "))

# Initialize first two terms
a = 0
b = 1
count = 1

# Generate Fibonacci series using while loop
while count <= n:
    print(a)
    next_term = a + b
    a = b
    b = next_term
    count += 1

#output
# Enter the number of terms: 10
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34