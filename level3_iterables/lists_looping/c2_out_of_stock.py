sandwichOrders = ["pastrami", "tuna", "pastrami", "chicken", "pastrami", "ham", "pastrami", "cheese", "pastrami"]

ingredients = ["chicken", "chicken", "tuna", "tuna", "ham", "ham", "cheese", "cheese"]

finishedOrders = []

while sandwichOrders:
    # print(ingredients)
    # print(sandwichOrders)
    order = sandwichOrders.pop()

    if order in ingredients:
        print(f"Here is your {order} sandwich.")
        ingredients.pop(ingredients.index(order))
        finishedOrders.append(order)
    else:
        print(f"Sorry, we have run out of {order}. You can choose a different sandwich.")

print()
print("All of the orders have been made. Here are all the finished orders:", finishedOrders)