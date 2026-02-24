# 1. Student Marks Analyzer

marks = [95, 85, 102, -5, 76, 88, 91]

# Remove invalid marks (0–100 only)
valid_marks = [m for m in marks if 0 <= m <= 100]

# Calculate average
average = sum(valid_marks) / len(valid_marks)

# Find topper
topper = max(valid_marks)

# Grade based on average
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "Fail"

print("Valid Marks:", valid_marks)
print("Average:", average)
print("Topper:", topper)
print("Grade:", grade)

# OUTPUT:
# Valid Marks: [95, 85, 76, 88, 91]
# Average: 87.0
# Topper: 95
# Grade: B