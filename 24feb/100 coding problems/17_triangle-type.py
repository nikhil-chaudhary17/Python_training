# Read three sides
a = int(input("Enter side a: "))
b = int(input("Enter side b: "))
c = int(input("Enter side c: "))

# Check if triangle is valid first
if a + b > c and a + c > b and b + c > a:
    
    # Check triangle type
    if a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")

else:
    print("Not a valid triangle")

#output
# Enter side a: 5
# Enter side b: 5
# Enter side c: 5
# Equilateral