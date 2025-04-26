currentUsers = ["John", "Dave", "Mr Sir", "Alex", "James", "Robert", "admin"]
# currentUsers = []

if not currentUsers == []:
    for name in currentUsers:
        if name == "admin":
            print("Hello, admin, would you like to see a status report?")
        else:
            print(f"Hello, {name}, thank you for logging in.")
else:
    print("Unfortunately, there are no users today.")