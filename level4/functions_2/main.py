def greetUser():
    print("Hello!")
greetUser()

def greetUser(username):
    print(f"Hello, {username.title()}!")
greetUser("alex")

print()

def favouriteBook(title):
    print(f"One of my favourite books is {title.title()}.")
favouriteBook("impossible creatures")

print()

def describePet(name, animalType):
    print(f"I have a {animalType}.")
    print(f"It's name is {name}.")
describePet("Gizmo", "dog")
describePet("lucy", "fish")
describePet("Jeremy", "tortoise")

def describePet(name, animalType = "cat"):
    print(f"I have a {animalType}.")
    print(f"It's name is {name}.")
describePet("Gizmo")