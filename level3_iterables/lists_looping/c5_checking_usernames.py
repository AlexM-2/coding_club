currentUsers = ["John", "Dave", "Alex", "James", "Robert", "admin"]
# currentUsers = []

newUsers = ["JOHN", "Admin", "Mr Sir"]

if not currentUsers == []:
    for user in currentUsers:
        if user == "admin":
            print("Hello, admin, would you like to see a status report?")
        else:
            print(f"Hello, {user}, thank you for logging in.")
else:
    print("Unfortunately, there are no users today.")

def listUpper(list):
    for string in list:
        list[list.index(string)] = string.upper()
    return list

print()

currentUsersUpper = listUpper(currentUsers)
if not newUsers == []:
    for user in newUsers:
        if user.upper() in currentUsersUpper:
            print(f"{user} is not a valid username")
            
        else:
            currentUsers.append(user)
        
print(currentUsers)