import random

superPowers = ["flight", "cool cape", "20/20 vision", "coding skills"]
print("Super powers include: ", *superPowers)

newPowers = ["strength", "persuasion", "super speed"]
randomPower = random.choice(newPowers)
print(f"Your superhero's power today is {randomPower}")

allPowers = superPowers.extend(newPowers)
print(f"All of the powers: ", *allPowers)