# Read number of terms
n = int(input("Enter the number of terms: "))

a = 0
b = 1

for i in range(n):
    print(a)
    c = a + b
    a = b
    b = c

# Example Input:
# 5
# Example Output:
# 0
# 1
# 1
# 2
# 3