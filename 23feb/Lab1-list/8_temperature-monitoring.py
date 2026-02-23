# 8. Temperature Monitoring System

temps = [35, 42, 46, 39, 50, 41]

hottest = max(temps)
coldest = min(temps)

# Replace above 45
for i in range(len(temps)):
    if temps[i] > 45:
        temps[i] = "Heat Alert"

extreme_days = len([t for t in temps if t != "Heat Alert" and t > 40])

print("Hottest:", hottest)
print("Coldest:", coldest)
print("Updated Temps:", temps)
print("Extreme Days:", extreme_days)

# OUTPUT:
# Hottest: 50
# Coldest: 35
# Updated Temps: [35, 42, 'Heat Alert', 39, 'Heat Alert', 41]
# Extreme Days: 2