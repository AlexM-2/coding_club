sandwichOrders = ["pastrami", "tuna", "pastrami", "chicken", "pastrami", "ham", "pastrami", "cheese", "pastrami"]

finishedOrders = []

while sandwichOrders:
    order = sandwichOrders.pop()
    print(f"Here is your {order} sandwich.")
    finishedOrders.append(order)

print()
print("All of the orders have been made.")