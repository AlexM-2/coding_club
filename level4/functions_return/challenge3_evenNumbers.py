a = 4
b = 7
c = 2
d = 4

def isEven(num):
    if num % 2 == 0:
        return "is even"
    else:
        return "is not even"

isEven1 = isEven(a)
isEven2 = isEven(b)
isEven3 = isEven(c)
isEven4 = isEven(d)

print(f"{a} {isEven1}.")
print(f"{b} {isEven2}.")
print(f"{c} {isEven3}.")
print(f"{d} {isEven4}.")