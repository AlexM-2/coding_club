#makes a list of friends
friends = ["Mary", "Josh", "Maddie", "Lucas", "Tom"]
print("<A list of friends has been created>")

print()

#looping through the list of friends
print("Looping through the friends:")
for friend in friends:
    print(friend)

print()

for friend in friends:
    print(f"Hello, {friend}")

print()
print("="*75)
print()

#creates a list of magicians
magicians = ["david", "harry", "lucia", "matthew"]
print("<A list of magicians has been created>")

print()

#looping through the list of magicians
print("Looping through the list of magicians:")
for magician in magicians:
    print(f"{magician.title()}, that was a great trick.")
    print(f'I can\'t wait to see your next trick, {magician.title()}!')
print("Thank you everyone, that was an amazing show.")