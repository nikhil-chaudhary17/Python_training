def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

num = int(input("Enter a number: "))

print("Sum of digits is:", sum_of_digits(num))

# Example:
# Enter a number: 123
# Sum of digits is: 6