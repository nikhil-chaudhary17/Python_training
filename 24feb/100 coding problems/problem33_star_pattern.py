# Read number of rows
n = int(input(""))

# Print star pattern
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()