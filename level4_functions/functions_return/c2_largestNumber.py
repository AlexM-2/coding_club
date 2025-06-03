a = 4
b = 7
c = 2
d = 4
manyNums = [4, 7, 8, 5.5, 1, 9]

def largestOfTwoNumbers(a, b):
    if a > b:
        pass

largestNum1 = largestOfTwoNumbers(a, b)
largestNum2 = largestOfTwoNumbers(c, d)
print(f"The largest of {a} and {b} is {largestNum1}")
print(f"The largest of {c} and {d} is {largestNum2}")

print()

def largest(numberList):

    total = 0
    itemsInList = 0

    for n in numberList:
        total+= n
        itemsInList+= 1

    return total / itemsInList

largestNum3 = largest([a, b])
largestNum4 = largest(manyNums)
print(f"The largest of {a} and {b} is {largestNum3}.")
print(f"The largest of {manyNums} is {largestNum4}.")