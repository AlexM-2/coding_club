import random

superPowers = ["flight", "cool cape", "20/20 vision", "coding skills"]
print("Super powers include: ", superPowers)

newPowers = ["strength", "persuasion", "super speed"]
randomPower = random.choice(newPowers)
print(f"Your superhero's extra power today is {randomPower}")
print("All of your superhero's powers today are: ", superPowers.append(randomPower))
print(f"All of your superhero's possible superpowers are: {superPowers.extend(newPowers)}")

print()

superheroName = input("What is your superhero's name?: ")
newSuperpower = input("What extra superpower do you want your superhero to have?: ")
newPowers.append(newSuperpower)
superPowers.append(newSuperpower)

randomPower = random.choice(newPowers)
print(f"All of your superhero's possible superpowers are now: {superPowers}")

print()

print(f"Your superhero is called {superheroName} and has {randomPower}")