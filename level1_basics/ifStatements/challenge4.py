number = float(input("Enter a number: "))
if number % 2 == 0:
    print("Your number is even.")
elif (number + 1) % 2 == 0:
    print("Your number is odd.")
else:
    print("Your number is a decimal.")