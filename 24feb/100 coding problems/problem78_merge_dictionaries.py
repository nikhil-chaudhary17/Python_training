dict1 = {}
n1 = int(input("Enter number of elements in first dictionary: "))

for i in range(n1):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict1[key] = value

dict2 = {}
n2 = int(input("Enter number of elements in second dictionary: "))

for i in range(n2):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict2[key] = value

# Manual merge
merged = {}

for key in dict1:
    merged[key] = dict1[key]

for key in dict2:
    merged[key] = dict2[key]

print("Merged dictionary:", merged)