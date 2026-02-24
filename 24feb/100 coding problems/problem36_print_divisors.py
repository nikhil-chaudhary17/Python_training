# Read number
n = int(input("Enter a number n: "))

# Print all divisors
for i in range(1, n + 1):
    if n % i == 0:
        print(i)

# Example Input:
# 6
# Example Output:
# 1
# 2
# 3
# 6