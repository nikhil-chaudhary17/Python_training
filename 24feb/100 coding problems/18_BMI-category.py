# Read weight (kg) and height (meters)
weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

# Calculate BMI
bmi = weight / (height * height)

# Determine category
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")

#output
# Enter weight in kg: 70
# Enter height in meters: 1.75
# Normal