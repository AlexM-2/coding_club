count = 0

#using a while loop to count to 5
print("Counting to 5 with a while loop:")
while count < 5:
    count += 1
    print(count)

print("="*50)

#terminating a loop with an if statement and break
print("Terminating a loop with an if statement and break:")
while True:
    someInput = input("Type 3 to continue, anything else to quit: ")
    if someInput == "3":
        print("Thank you for typing 3.")
    else:
        print("That's not 3, I'm quiting now")
        break

print("="*50)

#initialising variables
num = 1
total = 0

#using a while loop find the sum of numbers 1-10
while num<= 10:
    total+= num
    num+=1

print(f"The sum of numbers from 1-10 is {total}")

print("="*50)

target_number = 12
guess = None

print("My number is between 1 and 20")
print("My number is divisible by 12")

while guess != target_number:
    guess = int(input("Guess my number: "))

    if guess == target_number:
        print()
        print("You guessed my number!")
    else:
        print()
        print("Keep guessing")