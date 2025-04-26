import random

#creates lists for all the possible things a superhero generated from this can have
possibleAbilities = ["teleportation", "X-ray vision", "web shooters", "wall climbing abilities"]
possiblePlaces = ["London", "New York", "Paris"]
randomAbility = random.choice(possibleAbilities)
randomPlace = random.choice(possiblePlaces)

strength = random.randint(1,11)
stamina = random.randint(1,11)
speed = random.randint(1,11)
awareness = random.randint(1,11)

print(f"This superhero saves lives in {randomPlace}, has {randomAbility}, {strength} units of strength, \n{stamina} units of stamina, {speed} units of speed, {awareness} units of awareness.")