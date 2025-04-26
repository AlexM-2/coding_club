times_table = int(input("Which times table would you like me to calculate?: "))
times = list(range(0, (int(input("How many numbers should I go up to?: ")) + 1)))

print()

print(f"The {times_table} times table:")
for i in times:
    num = times_table * i
    print(f"{times_table} X {i} = {num}")