colouring_pencils = {"red":4, "yellow":3, "brown":2, "black":4}
print(f"Number of black colouring pencils: {colouring_pencils["black"]}")

print()

rewards = {"points":5, "lives":3, "coins":20}
newRewards = rewards["points"]
print("You have gained", newRewards, "new points!")

print()

player1 = {}
player1["colour"] = "red"
player1["lives"] = 5
player1["points"] = 10
print(player1)

print()

alien = {"colour":"green", "lives":5}
alien["x_position"] = 100
alien["y_position"] = 50
print(alien)

print(f"The alien colour is {alien["colour"]}.")
print("Changing colour of alien...")
alien["colour"] = "yellow"
print("The new alien colour is now:", alien["colour"], ".")

print()

fruit = {"apples":5, "bananas":8, "oranges":10, "melons":3}
print(fruit)
del fruit["melons"]
print(fruit)

print()

programming_languages = {
    "lucy":"python",
    "josh":"ruby",
    "matilda":"javaScript",
    "matthew":"C"
}
print(f"Lucy's top programming language is {programming_languages['lucy'].title()}")