recWidth = 400
recHeight = 100

recDimensions = (recWidth, recHeight)
print("The dimensions for this rectangle are:")
print(f"{recDimensions[0]}, {recDimensions[1]}")

print()

recWidth = 600
print("The tuple after trying to change it:")
print(f"{recDimensions[0]}, {recDimensions[1]}")

print()

#recDimensions[1] = 150
recDimensions = (600, 150)
print("The tuple after trying to change it again:")
print(f"{recDimensions[0]}, {recDimensions[1]}")

print()

numbers = (10,20,30,40,50,60,70,80,90,100)
print("A number tuple: ", numbers)

print()

print("Printing all the numbers in that tuple:")
for number in numbers:
    print(number)

print()

villains = ("The Sheriff of Nottingham", "Spike", "Not-so-happy-man", "Lonely Heart")
print("All the villains:")
print(villains[0])
print(villains[1])
print(villains[2])
print(villains[3])

print()

purpleCapes = ("purple frilly cape", "purple short cape", "purple cape with holes in it")
polkaCapes = ("black and white polka-dot cape", "white and beige polka-dot cape", "blue polka-dot cape")

allCapes = purpleCapes + polkaCapes
print("All of the capes including purple and polka-dot capes:")
print(allCapes)

print("The first item in the list:")
print(allCapes[0]*3)