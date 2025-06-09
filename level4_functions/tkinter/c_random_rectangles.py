from tkinter import Tk, Canvas, Button
from random import randint

tk = Tk()
width, height = 400, 400
canvas = Canvas(tk, width=width, height=height)
canvas.pack()

def generate_rectangles(count = 100, size = 2):
    
    canvas.delete("all")

    for i in range(count+1):

        rand_position = (randint(0, width), randint(0, height))
        rand_size = (randint(0, int(width//size)), randint(0, int(height//size)))

        x0 = rand_position[0] - (rand_size[0] / 2)
        y0 = rand_position[1] - (rand_size[1] / 2)

        x1 = rand_position[0] + (rand_size[0] / 2)
        y1 = rand_position[1] + (rand_size[1] / 2)

        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)

        canvas.create_rectangle(x0, y0, x1, y1, fill=(f"#{red:02x}{green:02x}{blue:02x}"))

button = Button(tk, text="Generate Art", command=generate_rectangles)
button.pack()

tk.mainloop()