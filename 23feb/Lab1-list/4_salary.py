# 4. Salary Processing System

salaries = [25000, 60000, 45000, 80000, 30000]

# Remove below minimum wage (30000)
salaries = [s for s in salaries if s >= 30000]

# Add 5% bonus if salary > 50000
for i in range(len(salaries)):
    if salaries[i] > 50000:
        salaries[i] *= 1.05

# Sort descending
salaries.sort(reverse=True)

print("Top 3 Salaries:", salaries[:3])

# OUTPUT:
# Top 3 Salaries: [84000.0, 63000.0, 45000]