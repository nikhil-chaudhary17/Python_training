# Initialize total sum
total = 0

# Read first number
num = int(input("Enter a number (0 to stop): "))

# Continue accepting numbers until 0 is entered
while num != 0:
    total += num
    num = int(input("Enter a number (0 to stop): "))

print(" Total sum:", total)