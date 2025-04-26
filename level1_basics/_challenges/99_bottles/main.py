bottles = 99

while True:
    print(f"{bottles} bottles of milk on the wall, {bottles} bottles of milk.")
    bottles-= 1

    if bottles == 0:
        print(f"Take one down, pass it around, no more bottles of milk on the wall.")
        print("No more bottles of milk on the wall, no more bottles of milk.")
        bottles = 99
        print(f"Go to the store and buy some more, {bottles} bottles of milk on the wall.")
    else:
        print(f"Take one down, pass it around, {bottles} of milk on the wall.")