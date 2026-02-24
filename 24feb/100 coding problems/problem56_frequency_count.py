numbers = list(map(int, input("Enter numbers separated by space: ").split()))

for num in numbers:
    count = 0
    for x in numbers:
        if x == num:
            count += 1
    print(num, "appears", count, "times")

# Example:
# Enter numbers separated by space: 1 2 2 3
# 1 appears 1 times
# 2 appears 2 times
# 2 appears 2 times
# 3 appears 1 times