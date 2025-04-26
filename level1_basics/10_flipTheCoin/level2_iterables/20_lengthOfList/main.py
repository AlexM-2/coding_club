#creates a list of strings
listOfStrings = ["apple", "banana", "strawberry", "cherry"]
print(f"Here is a list: {listOfStrings}")

#gets the length of the list
listLength = len(listOfStrings)
print(f"Here is the length of the list: {listLength}")

print()

#goes through all the strings in the list
for i in range(listLength):
   
	#gets a single name of the list
	currentString = listOfStrings[i]
	#prints that name
	print(f"String at index: {i}: {currentString}")

print()

#creates a list of names
names = ["Alice", "Bob", "Charlie", "David", "Eve"]

#length of the list of names
numNames = len(names)

#goes through all the names
for i in range(numNames):
   
	#gets the name
	currentName = names[i]
	#prints the name
	print(f"Hello, {currentName}!")