import random
import time

#creates and prints a random number between 0 and 10
randomNumber = random.randint(0,10)
print(f"A random number between 0-10: randomNumber")

print("="*50)


print("You are rolling a dice.")
time.sleep(0.5)
print("...")
time.sleep(0.5)

#creates and prints a random number between 1 and 6
randomNumber = random.randint(1,6)
print(f"You rolled a {randomNumber}!")