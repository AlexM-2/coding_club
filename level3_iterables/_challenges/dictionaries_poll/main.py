pollData = {}
popularity = {}

quit = False
firstPerson = True

def printDict(dictionary):
    for key, value in dictionary.items(): #iterates through dictionary and prints it's contents
        print(f"{key}         {value}")

while True:

    if quit == True: #stops the loop if the poll has finished
        break
    
    if pollData == {}:
        print("You are taking part in a poll about favourite foods. You are the first person to enter. Type and enter \"c\" to continue.")
        firstPerson = False
    else:
        print("You are taking part in a poll about favourite foods. Type and enter \"c\" to continue or \"q\" to quit.")

    if firstPerson == True:

        while True:
            response = input().upper()
            if not response == "C":
                continue
            else:
                break

    else:

        while True:
            response = input().upper()
            if response == "Q":
                quit = True
                break
            elif response == "C":
                break
    
    if quit == True: #stops the loop if the poll has finished
        break
    
    print()

    name = input("What is your name?: ").title()
    food = input("What is your favourite food?: ").title()

    pollData[name] = food

    if food in popularity:
        popularity[food]+= 1
    else:
        popularity[food] = 1
    
    print()

    print("Here are the current popularity scores for favourite foods. Type and enter \"c\" to continue or \"q\" to quit.")
    printDict(popularity)

    while True:
        response = input().upper()
        if response == "Q":
            quit = True
            break
        elif response == "C":
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"*1000)
            break

print("Here are the popularity scores and full data:")
printDict(popularity)
print()
printDict(pollData)