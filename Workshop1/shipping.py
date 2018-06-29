items = int(input("Enter the number of items"))
shipCost = 0

while items > 0:
    shipCost += float(input("Enter shipping cost $"))
    items -= 1

if shipCost >100:
    discount = shipCost * 0.1
    shipCost -= discount
    print(shipCost)
else:
    print(shipCost)