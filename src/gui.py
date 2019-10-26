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

        ncards=13
        self.cards = [[] for i in range(ncards)]
        for i in range(ncards):
            self.cards[i] = CardButton(self, command=self.test)
            self.cards[i].change_card(Card(1, i+2))
            self.cards[i].place(relx=1.0*i/ncards, rely=0.0, relwidth=1.0/ncards, relheight=1.0)

    def test(self):
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

        self.handDisplay = HandDisplay(parent)

        self.handDisplay.place(relx=0.0, rely=0.6, relheight=0.4, relwidth=1.0)

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
