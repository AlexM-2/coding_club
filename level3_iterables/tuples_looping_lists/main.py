people = [("Alice", 24, "New York"), ("Bob", 20, "London"), ("Luke", 23, "Paris")]
'''
for person in people:
    name = person[0]
    age = person[1]
    city = person[2]
    print(f"name = {name}, age = {age}, city = {city}")
'''
#another way to unpack a list of tuples:
for name, age, city in people:
    print(f"name = {name}, age = {age}, city = {city}")