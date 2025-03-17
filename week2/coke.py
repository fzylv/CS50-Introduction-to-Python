cost= 50
amount = 0

while amount < cost:
    print(f"Amount Due: {cost - amount}")
    coin= int(input("Insert coin: "))

    if coin == 25 or coin == 10 or coin==5:
        amount += coin
    else:
        print("Coin returned")

change = amount - cost
print(f"Change owed: {change}")
