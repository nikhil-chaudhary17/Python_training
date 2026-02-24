# Read base and power
base = int(input())
power = int(input())

result = 1

# Calculate power without using **
for i in range(power):
    result = result * base

print(result)

# Example Input:
# 2
# 3
# Example Output:
# 8