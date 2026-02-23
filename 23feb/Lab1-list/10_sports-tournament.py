# 10. Sports Tournament Points Table

points = [10, -5, 25, 15, 30]

# Replace negative with 0
points = [p if p >= 0 else 0 for p in points]

points.sort(reverse=True)

winner = points[0]
runner_up = points[1]

print("Leaderboard:", points)
print("Winner:", winner)
print("Runner Up:", runner_up)

# OUTPUT:
# Leaderboard: [30, 25, 15, 10, 0]
# Winner: 30
# Runner Up: 25