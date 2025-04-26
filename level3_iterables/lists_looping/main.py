availableToppings = ["mushrooms", "olives", "green peppers", "pepperoni", "pineapple", "extra cheese"]

requestedToppings = ["mushrooms", "french fries", "extra cheese"]

for topping in requestedToppings:
    if topping in availableToppings:
        print(f"Here are your {topping}.")
    else:
        print(f"Unfortunately, {topping} are not in the menu and we do not serve them. Sorry.")

print()

prompt = "Enter the name a a city you have visited before (enter q to quit): "

while True:

    response = input(prompt).upper()

    if response == "Q":
        break
    
    print(f"I'd love to go to {response.title()}!")

print()

unverifiedUsers = ["Martin", "Joe", "Alice"]
verifiedUsers = []

string = "All verified users:"
while unverifiedUsers:

    user = unverifiedUsers.pop()
    verifiedUsers.append(user)

    string = f"{string} {user},"

    print(f"Verified {user}.")
print(string)

print()

pets = ["dog", "cat", "dog", "goldfish", "cat", "rabbit", "cat"]

print(pets)
while "cat" in pets:
    pets.remove("cat")
    print(pets)