specialNumber = 23

numberList = []
numberList.append(specialNumber)
numberList.append(12)
numberList.append(specialNumber)
numberList.append(5)
print("Current list of numbers: ", numberList)

print()

if numberList.count(specialNumber) != 0:
    numberList.remove(specialNumber)
    print(f"Removed the first occurrance of {specialNumber}.")
    print("Updated list of numbers: ", numberList)

    print()

    print(f"The number {specialNumber} now appears {numberList.count(specialNumber)} time(s) in the list.")