from Tkinter import *
from PIL import Image

from game import Card


class CardButton:

    def __init__(self, master, card=Card(0, 0)):
        frame = Frame(master)
        frame.pack()

        self.button = Button(frame, command=self.change_image)
        self.button.config(image=images[1][12])
        self.button.pack(side=LEFT)

    def change_image(self):
        card = Card(2, 10)
        self.button.config(image=images[card.suit][card.value - 2])


class App:

    def __init__(self, master):
        frame1 = Frame(master, bg="red")
        frame2 = Frame(master, bg="green")
        frame3 = Frame(master, bg="blue")
        frame4 = Frame(master, bg="yellow")
        frame5 = Frame(master, bg="purple")

        frame1.place(relx=0.0, rely=0.0, relheight=0.3, relwidth=0.5)
        frame2.place(relx=0.5, rely=0.0, relheight=0.3, relwidth=0.5)
        frame3.place(relx=0.0, rely=0.3, relheight=0.3, relwidth=0.5)
        frame4.place(relx=0.5, rely=0.3, relheight=0.3, relwidth=0.5)
        frame5.place(relx=0.0, rely=0.6, relheight=0.4, relwidth=1.0)

        self.button = Button(
            frame1, text="QUIT", fg="red", command=frame1.quit
        )
        self.button.place(relx=0.1, rely=0.1)

        self.hi_there = Button(frame2, command=self.change_image)
        self.hi_there.config(image=images[2][12])
        self.hi_there.place(relx=0.1, rely=0.1)

    def change_image(self):
        print "hi there, everyone!"
        card = Card(3, 10)
        self.hi_there.config(image=images[card.suit][card.value - 2])


width = 800
height = 600


root = Tk()

# get card images
images = [[[] for j in range(13)] for i in range(4)]
suits = ['H', 'S', 'D', 'C']
values = [str(i) for i in range(2, 11)]
values.extend(['J', 'Q', 'K', 'A'])
for s in range(len(suits)):
    for v in range(len(values)):
        image_path = "images/" + values[v] + suits[s] + ".png"
        images[s][v] = PhotoImage(file=image_path)

canvas = Canvas(root, height=height, width=width)
canvas.pack()

app = App(root)

root.mainloop()
root.destroy()  # optional; see description below
