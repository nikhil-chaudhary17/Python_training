# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Input
num = int(input("Enter a number: "))

# Output
if is_prime(num):
    print("It is a Prime number")
else:
    print("It is not a Prime number")

# Example:
# Enter a number: 7
# It is a Prime number