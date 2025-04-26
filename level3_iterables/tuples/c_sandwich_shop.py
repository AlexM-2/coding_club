import time

theMenu = ("Apple sandwich", "Ham sandwich", "Salmon sandwich", "Banana sandwich", "Cheese sandwich")

print("Here is the menu:")
for food in theMenu:
    print("- ", food)

print()

#foods[1] = "potato"   -not including this line as it causes an error
print("Just making sure the menu can't be changed: ", theMenu)

time.sleep(1)
print()
print("...")
time.sleep(1)

print()


theMenu = ("Tuna sandwich", "Ham sandwich", "Salmon sandwich", "Random filling sandwich", "Cheese sandwich")
print('We\'ve decided to change our menu!')
print("Here is the updated menu:")
for food in theMenu:
    print("- ", food)