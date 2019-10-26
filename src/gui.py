import Tkinter as tk

from game import Card


class CardButton(tk.Button):

    def __init__(self, parent, command):
        tk.Button.__init__(self, parent, command=command)

    def change_card(self, card):
        self.config(image=images[card.suit][card.value - 2])


class HandDisplay(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="yellow")
        self.button = tk.Button(self, text="Button", fg="red", command=self.change_image())
        self.button.place(relx=0.5, rely=0.5)

    def change_image(self):
        print "button works"


class App:

    def __init__(self, parent):
        frame1 = tk.Frame(parent, bg="red")
        frame2 = tk.Frame(parent, bg="green")
        frame3 = tk.Frame(parent, bg="blue")
        frame4 = tk.Frame(parent, bg="yellow")

        frame1.place(relx=0.0, rely=0.0, relheight=0.3, relwidth=0.5)
        frame2.place(relx=0.5, rely=0.0, relheight=0.3, relwidth=0.5)
        frame3.place(relx=0.0, rely=0.3, relheight=0.3, relwidth=0.5)
        frame4.place(relx=0.5, rely=0.3, relheight=0.3, relwidth=0.5)

        self.button = tk.Button(
            frame1, text="QUIT", fg="red", command=frame1.quit
        )
        self.button.place(relx=0.1, rely=0.1)

        self.hi_there = tk.Button(frame2, command=self.change_image)
        self.hi_there.config(image=images[2][12])
        self.hi_there.place(relx=0.1, rely=0.1)

        self.testButton = CardButton(frame3, command=self.test)
        self.testButton.place(relx=0.2, rely=0.0)

        self.handDisplay = HandDisplay(parent)

        self.handDisplay.place(relx=0.0, rely=0.6, relheight=0.4, relwidth=1.0)

    def change_image(self):
        print "hi there, everyone!"
        card = Card(3, 10)
        self.hi_there.config(image=images[card.suit][card.value - 2])

    def test(self):
        card = Card(2, 2)
        self.testButton.change_card(card)

width = 800
height = 600


root = tk.Tk()

# get card images
images = [[[] for j in range(13)] for i in range(4)]
suits = ['H', 'S', 'D', 'C']
values = [str(i) for i in range(2, 11)]
values.extend(['J', 'Q', 'K', 'A'])
for s in range(len(suits)):
    for v in range(len(values)):
        image_path = "images/" + values[v] + suits[s] + ".png"
        images[s][v] = tk.PhotoImage(file=image_path)

# set initial size of the window
canvas = tk.Canvas(root, height=height, width=width)
canvas.pack()

app = App(root)

root.mainloop()
root.destroy()  # optional; see description below
