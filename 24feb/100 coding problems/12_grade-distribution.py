# Read marks from standard input
marks = int(input("Enter marks: "))

# Check grade conditions
if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
elif marks >= 35:
    print("Grade D")
else:
    print("Fail")

# output
# Enter marks: 85
# Grade A