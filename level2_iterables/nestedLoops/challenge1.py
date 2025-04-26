foods = ["pizza", "noodles", "donut", "toast"]

drinks = ["water", "orange juice" ,"coffee", "soda"]

for food in foods:
    for drink in drinks:
        if food == "pizza" and drink == "soda":
            print("The perfect combo, pizza and soda.")
        elif drink == "coffee" and food != "donut":
            continue
        else:
            print(f"How about {food} and {drink}?")