adjectives = ["enormous", "happy", "sleepy", "curious", "playful"]
animals = ["cat", "dog", "rabbit", "elephant"]

enormousElephantPrinted = False

for adjective in adjectives:
    for animal in animals:
        if animal != "elephant" and adjective == "enormous":
            continue
        else:
            print(f"{adjective} {animal}")