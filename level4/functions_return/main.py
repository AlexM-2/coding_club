a = 4
b = 7
c = 2
d = 4
e = 5
f = 6

def add(num1, num2):
    return num1 + num2

sum1 = add(4, 7)
sum2 = add(2, 4)
print(f"The sum of 4 and 7 is {sum1}.")
print(f"The sum of 2 and 4 is {sum2}.")

print()

def rectangleArea(length, height):
    return length * height

area1 = rectangleArea(a, b)
area2 = rectangleArea(c, d)
print(f"The area of a rectangle with length of 4cm and height of 7cm is {area1}cm^2.")
print(f"The area of a rectangle with length of 2cm and height of 4cm is {area2}cm^2.")

print()

def boxVolume(length, width, height):
    return length * width * height

volume1 = boxVolume(a, e, b)
volume2 = boxVolume(c, f, d)
print(f"The volume of a box with a length of 4cm, width of 5cm and height of 7cm is {volume1}cm^3.")
print(f"The volume of a box with a length of 2cm, width of 6cm and height of 4cm is {volume2}cm^3.")

print()

product1 = rectangleArea(a, b)
product2 = rectangleArea(c, d)
print(f"The product of 4 and 7 is {product1}.")
print(f"The product of 2 and 4 is {product2}.")