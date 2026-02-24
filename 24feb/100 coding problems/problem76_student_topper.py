n = int(input("Enter number of students: "))

marks = {}

for i in range(n):
    name = input("Enter student name: ")
    score = int(input("Enter marks: "))
    marks[name] = score

topper = max(marks, key=marks.get)

print("Topper is:", topper)
print("Marks:", marks[topper])

# Example:
# Topper is: Rahul
# Marks: 95