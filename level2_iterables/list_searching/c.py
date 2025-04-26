#creates a list of numebers
numbers = [1,2,4,5,6,8,9]
print("<A list of numbers has been created>")

print()

#checks if 3 is in the list
if 3 in numbers:
    print("3 is in the list.")
else:
    print("3 is not in the list.")
    numbers.append(3)

print()

print("The updated list:")
print(numbers)