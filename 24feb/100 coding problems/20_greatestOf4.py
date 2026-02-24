# Read four numbers
a = int(input("Enter FIRST  numbers: "))
b = int(input("Enter SECOND numbers: "))
c = int(input("Enter THIRD numbers: "))
d = int(input("Enter FOURTH numbers: "))

# Find greatest
greatest = a

if b > greatest:
    greatest = b
if c > greatest:
    greatest = c
if d > greatest:
    greatest = d

print(greatest)