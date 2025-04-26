totalInventoryValue = 0
inventory = [
    ("Apples", 12, 0.8, 0.5),
    ("Bananas", 15, 0.7, 0.4),
    ("Oranges", 9, 1, 0.7),
    ("Pineapples", 5, 0.9, 1.5),
    ("Strawberries", 23, 0.5, 0.3),
    ("Mangoes", 9, 0.6, 1),
    ("Blackberries", 26, 0.8, 0.3)
]
for name, quantity, quality, price in inventory:
    totalProductPrice = quantity*price*quality
    print(f"Product: {name}, Quantity: {round(quantity, 2)}, Quality: {round(quality, 2)}, Price per item: £{round(price, 2)}, Total product value: £{round(totalProductPrice, 2)}")
    totalInventoryValue+= totalProductPrice
print()
print(f"The total inventory value is £{totalInventoryValue}")