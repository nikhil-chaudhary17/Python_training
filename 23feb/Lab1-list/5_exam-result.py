# 5. Online Exam Result Processor

scores = [25, 35, 40, 55, 30, 20, 70]

# Remove lowest 2 scores
scores.sort()
scores = scores[2:]

# Add grace marks
for i in range(len(scores)):
    if 30 <= scores[i] <= 35:
        scores[i] += 5

# Count pass students
passed = len([s for s in scores if s >= 40])

print("Updated Scores:", scores)
print("Number of Passed Students:", passed)

# OUTPUT:
# Updated Scores: [35, 40, 55, 70]
# Number of Passed Students: 4