stocks = {"AAPL": 180, "TSLA": 250, "GOOG": 140}

total = 0

print("Simple Stock Tracker")

while True:
    name = input("Enter stock name (or 'done'): ").upper()
    
    if name == "DONE":
        break
    
    if name in stocks:
        qty = int(input("Enter quantity: "))
        total += stocks[name] * qty
    else:
        print("Stock not found")

print("Total Investment:", total)