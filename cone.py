import threedfigures
import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)   # slant height

print("Curved Surface Area:", threedfigures.cone_csa(r, l))
print("Total Surface Area:", threedfigures.cone_tsa(r, l))
print("Volume:", threedfigures.cone_volume(r, h))