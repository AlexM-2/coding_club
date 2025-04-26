person = {
    "firstName":"Dulcie",
    "lastName":"Mascord",
    "village/town/city":"Clevedon",
    "age":21 #not actually 21
}

print(f"{person["firstName"]}'s full name is {person["firstName"] + " " + person["lastName"]}.")
print(f"{person["firstName"]} is {person["age"]} years old.")
print(f"{person["firstName"]} lives in {person["village/town/city"]}")