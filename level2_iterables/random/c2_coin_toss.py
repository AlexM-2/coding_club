import random
import time

coin = ["heads", "tails"]

while True:
    print("Computer is spinning a coin.")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    p1Rand = random.choice(coin)
    print(f"Computer got {p1Rand}")

    print("Player is spinning a coin.")
    time.sleep(0.5)
    print("...")
    time.sleep(0.5)
    p2Rand = random.choice(coin)
    print(f"Player got {p2Rand}")

    if p1Rand == p2Rand:
        print()
        print("You win!")
        break
    else:
        print()
        print("Try again")