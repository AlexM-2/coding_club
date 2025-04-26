superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.append("stretchy")
print("All of the superpowers: ", *superPowers)

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.insert(1, "healing")

print("Superpowers after inserting at index 1:")
print(*superPowers)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.pop(3)

print("Superpowers after removing the 3rd index using .pop():")
print(*superPowers)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.reverse()

print("Superpowers after reversing the order:")
print(*superPowers)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.sort()

print("Superpowers after sorting in alphabetical order:")
print(*superPowers)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.count("night vision")

print(f"Superpowers: ", *superPowers)
print(f"How many times 'night vision' appears in superpowers: {superPowers.count("night vision")}")

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
newSuperPowers = ["teleportation", "x-ray vision"]
superPowers.extend(newSuperPowers)

print("Superpowers after extending it with newSuperPowers:")
print(*superPowers)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers2 = superPowers.copy()

print("A copy of superpowers:")
print(*superPowers2)

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
print("The index of the item 'cool cape: ", superPowers.index("cool cape"))

print()

superPowers = ["regeneration", "cool cape", "night vision", "coding skills"]
superPowers.clear

print("Superpowers after clearing everything in the list:")
print(*superPowers)