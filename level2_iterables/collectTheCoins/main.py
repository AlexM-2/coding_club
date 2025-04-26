import random
import time

total = 0

while True:
    time.sleep(1)
    coinsGain = random.randint(0,3)
    total+= coinsGain
    print(f"You gained {coinsGain} coins!")
    print(f"You now have {total} coins.")
    print()
    if total >= 10:
        print("You reached 10 coins!")
        break