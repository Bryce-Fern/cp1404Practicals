total = 0
items = int(input("Number of items: "))

while items < 0:
    print("Please enter at least 1 item")
    items = int(input("Number of items: "))
for i in range(items):
        price = float(input("Price of item: $"))
        total += price
if total > 100:
    total = total * 0.9
    print("Total price for", items, "is: ", total)
else:
    print("Total price for", items, "is: ", total)