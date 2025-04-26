#creating a list
luckyNumbers = [7, 5, 9, 21]
print(luckyNumbers)

print()

#appending to lists
friends= ["Mary", "John", "Katie", "Lucy"]
friends.append("Rose")
print(friends)

print()

#lists can include anything
myList = [1, "Hello", luckyNumbers, friends]
print(myList)

print()

#you can get an item of a list using it's index
letters = ["a", "b", "c", "d", "e", "f", "g", "h"]
print(letters[0])
print(letters[2])

print()

#this prints a 'slice' of the list
print(letters[1:4])
print(letters[:3])
print(letters[4:])

print()

#you can assign an item in a list using it's index
myList[1] = "Hello World!"

#adding items on the end of the letters list
letters.extend(["i", "j", "k"])

#.insert takes 2 parameters: the index of the item in the list to be replaced, what it is going to be replaced with
myList.insert(1, 2)
print(myList)

print()

#deleting an item of the list using the list item
letters.remove("c")

#deleting an item of the list using it's index
del letters[0]
print(letters)

print()

#.pop deletes the last item of the list and moves it to whatever it is being used for
lastLetter = letters.pop()
print(letters)
print("I'm here, " + lastLetter)