# PROJECT 1: Stock Gain/Loss Calculator
# GOAL: Given a buy price and current price, compute the profit/loss
# in rupees and as a percentage.
print("=" * 55)
print("PROJECT 1: Stock Gain/Loss Calculator")
print("=" * 55)

buy_price = float(input("Buy Price (₹): "))
current_price = float(input("Current Price (₹): "))
shares = int(input("Number of shares: "))

invested = buy_price * shares
current_value = current_price * shares
profit = current_value - invested
pct_change = (current_price - buy_price) / buy_price * 100

print(f"\nInvested:      ₹{invested:,.2f}")
print(f"\nCurrent Value: ₹{current_value:,2f}")
print(f"\nProfit/Loss:   ₹{profit:,2f}")

if profit > 0:
    print("You are in Profit.")
elif profit < 0:
    print("You are in Loss.")
else:
    print("Break even - No gain - No loss.")