# Read number and range values
num = int(input("Enter a number: "))
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))

# Check range
if lower <= num <= upper:
    print("Within Range")
else:
    print("Outside Range")

#output
# Enter a number: 5
# Enter lower bound: 1
# Enter upper bound: 10
# Within Range