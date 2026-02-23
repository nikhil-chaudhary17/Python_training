# 6. Inventory Management

stock = [0, 5, 20, 8, 50]

# Remove 0 stock
stock = [s for s in stock if s > 0]

# Add restock (50 units) to items below 10
for i in range(len(stock)):
    if stock[i] < 10:
        stock[i] += 50

total_inventory = sum(stock)

print("Updated Stock:", stock)
print("Total Inventory:", total_inventory)

# OUTPUT:
# Updated Stock: [55, 20, 58, 50]
# Total Inventory: 183