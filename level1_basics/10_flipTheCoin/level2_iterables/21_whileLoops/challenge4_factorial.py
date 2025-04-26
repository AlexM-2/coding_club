inputNum = int(input("Enter an integer: "))
num = inputNum
count = inputNum

while True:
    if count < 2:
        break
    count-= 1
    num*= count

print(f"The factorial of {inputNum} is {num}")