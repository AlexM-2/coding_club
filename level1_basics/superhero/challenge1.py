import random

superPowers = ["flight", "cool cape", "20/20 vision", "coding skills"]
print("Super powers include: ", *superPowers)

newPowers = ["strength", "persuasion", "super speed"]
randomPower = random.choice(newPowers)
print(f"Your superhero's power today is {randomPower}")

print()

superheroName = input("What is your superhero's name?: ")
newPowers.append(input("What extra superpower do you want your superhero to have?: "))
randomPower = random.choice(newPowers)

print()

print(f"Your superhero is called {superheroName} and has {randomPower}")