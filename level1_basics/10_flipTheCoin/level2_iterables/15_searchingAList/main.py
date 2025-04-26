#creates a list of friends
friends = ["jonas", "rose", "lucas", "alba", "jack"]
print("<A list of friends has been created>")

print()

#searches the list for the name mary
if "mary" in friends:
    print("Mary is in the list.")
else:
    print("Add Mary to the list.")
    friends.append("mary")

print()

#searches the list for the name mary again
if "mary" in friends:
    print("Mary is in the list.")
else:
    print("Add Mary to the list.")
    friends.append("mary")

print()

#searches the list for the name alex
if "alex" in friends:
    print("Alex is in the list.")
else:
    print("Add Alex to the list.")
    friends.append("alex")

print()
print("="*75)
print()

#creates a list of letters
letters = ["a", "b", "c", "d", "e", "f", "g"]
print("<A list of letters has been created>")

print()

#checks if g is in the list
if "g" in letters:
    print("The letter g is in the list")
    letters.remove("g")

print("The updated list:")
print(letters)

print()

#finding the index of one of the items in the list
print("The index of the 'd' in the list")
print(letters.index("d"))