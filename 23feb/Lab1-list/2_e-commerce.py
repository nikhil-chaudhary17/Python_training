# 2. E-Commerce Cart System

cart = [2000, 3000, 2000, 1500]

# Remove duplicate items
cart = list(set(cart))

total = sum(cart)

# Apply 10% discount if total > 5000
if total > 5000:
    total = total * 0.9

# Add 18% GST
final_amount = total * 1.18

print("Final Payable Amount:", final_amount)

# OUTPUT:
# Final Payable Amount: 6372.0