def getTimesTableList(timesTable, num):

    timesTableList = []

    for n in range(1, num):
        timesTableList.append(n * timesTable)
    
    return timesTableList

def getTimesTableString(timesTable, num):

    timesTableString = ""

    for n in range(1, num):
        if not timesTableString == "":
            timesTableString = timesTableString + ", " + str(n * timesTable)
        else:
            timesTableString = timesTableString + str(n * timesTable)
    
    return timesTableString

def getTimesTable(timesTable, num):
    timesTableString = getTimesTableString(timesTable, num)
    if len(timesTableString) > 100:
        return [getTimesTableList(timesTable, num), "list"]
    else:
        return [timesTableString, "string"]

while quit:
    timesTable = input("What times table do you want to calculate? (type q to quit): ")
    if timesTable.upper() == "Q":
        quit()

    num = input(f"How many instances of the {timesTable} times table do you want to calculate? (type q to quit): ")
    if num.upper() == "Q":
        quit()

    timesTableNumbers = getTimesTable(int(timesTable), int(num))

    print()
    print(f"Here are {num} instances the {timesTable} times table: ")
    
    typeOfTable = timesTableNumbers[1]
    value = timesTableNumbers[0]
    if typeOfTable == "string":
        print(value)
    elif typeOfTable == "list":
        for n in value:
            if not n / int(timesTable) == num:
                print(str(n) + ",")
            else:
                print(n)
    else:
        print("ERROR")
        quit()