a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

# a,b = b,a

a = a + b
b = a - b
a = a - b

# values after swapping 

print("Value of a: ",a)
print("Value of b: ",b)

#output
# Enter value of a: 5
# Enter value of b: 10
# Value of a:  10
# Value of b:  5