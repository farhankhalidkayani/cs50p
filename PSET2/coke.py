Amount = 50
while Amount > 0:
    print(f"Amount Due: {Amount}")
    coin = int(input("Inset coin: "))
    if coin in (50, 25, 15, 10, 5):
        Amount -= coin
if Amount <= 0:
    print(f"Change Owed: {-1*Amount}")
