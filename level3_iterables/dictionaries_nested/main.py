users = {
    1: {"name": "Alice", "age": 25, "email": "alice@example.com"},
    2: {"name": "Bog", "age": 30, "email": "bob@example.com"},
    3: {"name": "Charlie", "age": 22, "email": "charile@example.com"},
    4: {"name": "Diana", "age": 28, "email": "diane@example.com"},
    5: {"name": "Ethan", "age": 35, "email": "ethan@example.com"},
    6: {"name": "Bruno", "age": 20, "email": "bruno@example.com"},
}
users[7] = {"name": "mary", "age": 18, "email": "mary@example.com"}
users[2]["email"] = "bob2@example.com"
del users[3]

print("="*25)
for userID, userInfo in users.items():
    print(f"UserID:", userID)
    print("Name:", userInfo["name"])
    print("Age:", userInfo["age"])
    print("Email address:", userInfo["email"])
    print("="*25)