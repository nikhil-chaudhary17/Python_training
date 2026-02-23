import threedfigures

l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
h = float(input("Enter height: "))

print("Total Surface Area:", threedfigures.cuboid_surface_area(l, b, h))
print("Volume:", threedfigures.cuboid_volume(l, b, h))