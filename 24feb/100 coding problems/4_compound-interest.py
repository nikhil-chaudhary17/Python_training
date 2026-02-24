# Read principal, rate, time
P = float(input("enter principal: "))
R = float(input("enter rate: "))
T = float(input("enter time: "))

# Calculate Compound Interest
CI = P * (1 + R / 100) ** T - P

print("Compound Interest is:", CI)

# output
# enter principal: 1000
# enter rate: 5
# enter time: 2
# Compound Interest is: 102.5