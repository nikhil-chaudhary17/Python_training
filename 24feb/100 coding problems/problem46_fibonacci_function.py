def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a)
        c = a + b
        a = b
        b = c

num = int(input("Enter number of terms: "))

print("Fibonacci Series:")
fibonacci(num)

# Example:
# Enter number of terms: 5
# Fibonacci Series:
# 0
# 1
# 1
# 2
# 3