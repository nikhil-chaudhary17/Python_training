# 7. Bank Transaction Analyzer

transactions = [10000, -2000, 15000, -5000, 8000]

total_balance = sum(transactions)

# Largest withdrawal
withdrawals = [t for t in transactions if t < 0]
largest_withdrawal = min(withdrawals)

# Deposits > 10000
big_deposits = len([t for t in transactions if t > 10000])

print("Total Balance:", total_balance)
print("Largest Withdrawal:", largest_withdrawal)
print("Deposits > 10000:", big_deposits)

# OUTPUT:
# Total Balance: 26000
# Largest Withdrawal: -5000
# Deposits > 10000: 1