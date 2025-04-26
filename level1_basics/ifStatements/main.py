temperatature = 30

if temperatature >= 30:
    print("It's hot!")
    print("Why don't we go to the beach")
else:
    print("It's cool in here.")

print()

age = int(input("Enter your age: "))

if age >= 18:
    print("You can watch any movies.")
elif age >= 16:
    print("You can watch any movies with a 16 rating.")
elif age >= 12:
    print("You can watch any movies with a 12 rating.")
elif age < 12:
    print("You can watch movies suitable for children.")