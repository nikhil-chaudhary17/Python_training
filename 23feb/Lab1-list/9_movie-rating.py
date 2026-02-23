# 9. Movie Rating System

ratings = [5, 4, 3, 6, 2, 5, 0]

# Remove invalid ratings (1–5)
ratings = [r for r in ratings if 1 <= r <= 5]

average = sum(ratings) / len(ratings)

five_star = ratings.count(5)

ratings.sort()

print("Valid Ratings:", ratings)
print("Average Rating:", average)
print("5-Star Count:", five_star)

# OUTPUT:
# Valid Ratings: [2, 3, 4, 5, 5]
# Average Rating: 3.8
# 5-Star Count: 2