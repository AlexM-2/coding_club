from tkinter import Tk, Button, Canvas

def hello():
    print("You have clicked the button.")

tk = Tk()

canvas = Canvas(tk, width=400, height=400)
canvas.pack()

canvas.create_line(0, 200, 400, 200)
canvas.create_line(200, 0, 200, 400)

canvas.create_rectangle(50, 50, 350, 350)
canvas.create_rectangle(100, 100, 300, 300, fill="#808080")

canvas.create_line(100, 100, 300, 150)
canvas.create_line(300, 100, 250, 300)
canvas.create_line(300, 300, 100, 250)
canvas.create_line(100, 300, 150, 100)

# button = Button(tk, text="CLICK ME!", command=hello)
# button.pack()

tk.mainloop()