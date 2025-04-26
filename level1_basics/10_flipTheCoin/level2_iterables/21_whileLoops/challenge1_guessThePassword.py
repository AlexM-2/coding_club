super_secret_password = "password"

attempts = 0

while True:
    super_secret_password_attempt = input("What is the password for access into the super secret spy cooperation?: ")
    if super_secret_password_attempt == super_secret_password:
        print("Welcome to the super secret spy cooperation.")
        break
    else:
        if attempts < 1:
            print("That is NOT the password into the super secret spy cooperation.")
            print("I will give you one more chance...")
            attempts+= 1
        elif attempts > 0:
            print("That is NOT the password into the super secret spy cooperation.")
            print("How dare you try and sneak in.")
            break
        else:
            print("ERROR")