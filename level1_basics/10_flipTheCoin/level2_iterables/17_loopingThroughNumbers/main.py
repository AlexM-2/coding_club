#prints a range of numbers (1-5)
print("Prints a range of numbers (1-5):")
for number in range(1,6):
	print(number)
  
print("="*50)

#prints a list of numbers using the range() function
print("Prints a list of numbers:")
numbers = list(range(1,11))
print(numbers)

print("="*50)

#prints a list of even numbers using the third parameter
print("Prints a list of even numbers using the third parameter:")
evenNumbers = list(range(0, 11, 2))
print(evenNumbers)

print("="*50)

#prints a list of square numbers
print("Prints a list of square numbers:")
squareNumbers = []
for value in range(1, 11):
	square = value**2
	squareNumbers.append(square)
print(squareNumbers)

print("="*50)

#prints a list of numbers
print("Prints a list of numbers:")
numbers = list(range(1, 11))
print(numbers)

print("*"*20)

#prints the smallest number in the list
print("Prints the smallest number in the list:")
print(min(numbers))

print("*"*20)

#prints the biggest number in the list
print("Prints the biggest number in the list:")
print(max(numbers))

print("*"*20)

#prints the sum of all the numbers in the list
print("Prints the sum of all the numbers in the list:")
print(sum(numbers))