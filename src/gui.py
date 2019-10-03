from Tkinter import *
from game import Card


class App:

    def __init__(self, master):

        frame = Frame(master)
        frame.pack()

        # get card images
        #self.images = [[] for i in range(4)]
        self.images = [[[] for j in range(13)] for i in range(4)]
        suits = ['H', 'S', 'D', 'C']
        values = [str(i) for i in range(2, 11)]
        values.extend(['J', 'Q', 'K', 'A'])
        for s in range(len(suits)):
            for v in range(len(values)):
                image_path = "images/" + values[v] + suits[s] + ".png"
                self.images[s][v] = PhotoImage(file=image_path)

        self.button = Button(
            frame, text="QUIT", fg="red", command=frame.quit
            )
        self.button.pack(side=TOP)

        self.hi_there = Button(frame, command=self.change_image)
        self.hi_there.config(image=self.images[2][12])
        self.hi_there.pack(side=TOP)

    def change_image(self):
        print "hi there, everyone!"
        card = Card(3, 10)
        self.hi_there.config(image=self.images[card.suit][card.value-2])


root = Tk()

app = App(root)

root.mainloop()
root.destroy()  # optional; see description below
