directory = {
    "John":7547947947,
    "Señor Peréz":727835953
}
directory["Señora Bond"] = 73481982
directory["Señorita Kellsall"] = 72893425389
directory["Mr John"] = 73492893274


def print_dir(dir):
    print()
    print("Here is your updated current phone directory:")
    for name, number in dir.items():
        print(f"\t{name}: {number}")
    print()

print("Here is your current phone directory:")
for name, number in directory.items():
    print(f"\t{name}: {number}")
print()


#entering more contacts
while True:
    name = input("Would you like to add another contact to your phone directory? If so, enter the name here, if not enter \"q\": ")
    if name.lower() == "q":
        break
    else:
        number = input("Enter the phone number of your desired contact: ")
        if number.lower() == "q":
            break
        else:
            directory[name] = number
            print_dir(directory)