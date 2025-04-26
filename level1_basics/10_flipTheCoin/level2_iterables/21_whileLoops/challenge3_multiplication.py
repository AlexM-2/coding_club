count = 1

multiplication = int(input("Enter an integer between 1 and 12: "))
print(f"Here are all {multiplication} times table:")

if multiplication > 0 and multiplication < 13:
    while count < 13:
        print(f"{multiplication} X {count} = {multiplication*count}")
        count+= 1
else:
    print()