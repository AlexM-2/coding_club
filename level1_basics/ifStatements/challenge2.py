weather = input("What is the weather like today?: ")

'''
cloudy
sunny
rainy
snowy
'''

if weather == "cloudy":
    print("Yes, it does look a bit dull today, doesn't it.")
elif weather == "sunny":
    print("It is sunny, you should wear your sunglasses.")
elif weather == "rainy":
    print("You should put your raincoat on.")
elif weather == "snowy":
    print("You need your snow boots today!")
else:
    print("I don't know that type of weather.")