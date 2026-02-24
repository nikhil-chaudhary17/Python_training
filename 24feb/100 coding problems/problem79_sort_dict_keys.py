n = int(input("Enter number of elements: "))
d = {}

for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    d[key] = value

sorted_keys = sorted(d.keys())

print("Dictionary sorted by keys:")
for key in sorted_keys:
    print(key, ":", d[key])