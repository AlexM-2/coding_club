guests = ["Mum", "Dad", "James"]

print(f"Would you like to come to dinner, {guests[0]}?")
print(f"Would you like to come to dinner, {guests[1]}?")
print(f"Would you like to come to dinner, {guests[2]}?")

print()
print("Unfortunately, James cannot make it")
print()

guests[2] = "Oliver"

print(f"Would you like to come to dinner, {guests[0]}?")
print(f"Would you like to come to dinner, {guests[1]}?")
print(f"Would you like to come to dinner, {guests[2]}?")