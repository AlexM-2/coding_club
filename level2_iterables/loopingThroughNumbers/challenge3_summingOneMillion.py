#creates a list of numbers from 1 to 1000000
oneMillionNumbers = range(1,1000001)
print("[A list with numbers 1-1000000 has been created]")
print()
print()
	
#prints the smallest number in the list
print("Prints the smallest number in the list - to make sure it actually starts at 1:")
print(min(oneMillionNumbers))
print()

#prints the biggest number in the list
print("Prints the biggest number in the list - to make sure it actually ends at 1000000:")
print(max(oneMillionNumbers))

#prints the sum of all the numbers
print("Prints the sum of all the numbers:")
print(sum(oneMillionNumbers))