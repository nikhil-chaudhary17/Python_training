n = int(input("Enter number of elements: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = int(input("Enter value: "))
    d[key] = value

sorted_items = sorted(d.items(), key=lambda item: item[1])

print("Dictionary sorted by values:")
for key, value in sorted_items:
    print(key, ":", value)