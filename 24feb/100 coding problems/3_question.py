a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
c = int(input("Enter value of c: "))

if(a > b and a > c):
    print(a," is greatest among all")
elif(b > a and b > c):
    print(b," is greatest among all")
else:
    print(c," is greatest among all")

# output
# Enter value of a: 5
# Enter value of b: 10
# Enter value of c: 15
# 15  is greatest among all