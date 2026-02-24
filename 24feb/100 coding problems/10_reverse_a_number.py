n = int(input("Entere a number : "))

# Reverse the number
reverse = 0

while n > 0:
    rem = n % 10
    reverse = reverse * 10 + rem
    n = n // 10

print("Reverse of the number is:", reverse)

#output
#enter a number : 12345
#Reverse of the number is: 54321