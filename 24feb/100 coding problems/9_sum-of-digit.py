n = int(input("Enter a number: "))

# Calculate sum of digits
sum_of_digits = 0
while n > 0:
    digits = n % 10
    sum_of_digits += digits
    n = n // 10
print("Sum of digits is:", sum_of_digits)
