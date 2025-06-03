a = 4
b = 7
c = 2
d = 4
numList1 = [4, 7]
numList2 = [4, 7, 8, 5.5, 1, 9]

def averageOfTwoNumbers(num1, num2):
    return (num1+num2) / 2

average1 = averageOfTwoNumbers(a, b)
average2 = averageOfTwoNumbers(c,d)
print(f"The average of {a} and {b} is {average1}")
print(f"The average of {c} and {d} is {average2}")

print()

def average(numberList):

    total = 0
    itemsInList = 0

    for n in numberList:
        total+= n
        itemsInList+= 1

    return total / itemsInList

average3 = average(numList1)
average4 = average(numList2)
print(f"The average of {numList1} is {average3}.")
print(f"The average of {numList2} is {average4}.")