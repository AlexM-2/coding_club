import time

specialPassword = "TheUltimatePassword"

print("Hello, welcome to the password pickers.")
time.sleep(1)
print("You can either use the basic password picker or the advanced password picker.")
time.sleep(2)
print("But to use the advanced password picker, you need to have the special password.")
time.sleep(2)

whichPasswordPicker = input("Would you like to use the basic password picker or the advanced password picker? (b/a): ")

if whichPasswordPicker == "b" or whichPasswordPicker == "B":
  print("Loading Basic Password Picker...")
  time.sleep(3)
  print(" ")
  import basicPasswordPicker
elif whichPasswordPicker == "a" or whichPasswordPicker == "A":
  specialPasswordAttempt = input("Special password: ")
  if specialPasswordAttempt == specialPassword:
    print("Correct password. Loading advanced password picker...")
    time.sleep(4)
    print(" ")
    import ultimatePasswordPicker
  else:
    print("Incorrect password. Exiting...")
    print()
    print("="*100)
    exit()
else:
  print("Invalid input. Exiting...")
  print()
  print("="*100)
  exit()