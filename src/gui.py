#!/usr/bin/env python

import Tkinter as tk

from functools import partial

from game import Card, Game
from player import ManualPlayer, AutoPlayer

images = []
backs = []
colors = ["red", "blue", "yellow", "green"]
game = Game()


class CardButton(tk.Button):

    def __init__(self, parent, command):
        tk.Button.__init__(self, parent, command=command)

    def change_card(self, card):
        if isinstance(card, Card):
            self.config(image=images[card.suit][card.value - 2])
        elif isinstance(card, int):
            self.config(image=backs[card])
        else:
            print ("wrong input to change_card function. {}".format(card))


class HandDisplay(tk.Frame):

    def __init__(self, parent):
        tk.Frame.__init__(self, parent, bg="yellow")

        ncards=13
        self.cards = [[] for i in range(ncards)]
        for i in range(ncards):
            self.cards[i] = CardButton(self, command=partial(self.play, i))
            self.cards[i].change_card(Card(1, i+2))
            self.cards[i].place(relx=1.0*i/ncards, rely=0.05, relwidth=1.0/ncards, relheight=0.9)
        self.show_hand()

    def play(self, i):
        global game
        p = game._players[game.next_player]
        card = p.play(i, game.suit)
        if card:
            game.play(p.id, card)

        self.show_hand()

    def show_hand(self):
        next_player = game.next_player
        self.config(bg=colors[next_player])
        hand = game._players[next_player].hand
        for i in range(len(self.cards)):
            if i < len(hand):
                self.cards[i].change_card(hand[i])
            else:
                self.cards[i].change_card(next_player)


class App:

    def __init__(self, parent):
        self.setup_game()

        frame1 = tk.Frame(parent, bg="red")
        frame2 = tk.Frame(parent, bg="green")
        frame3 = tk.Frame(parent, bg="blue")
        frame4 = tk.Frame(parent, bg="yellow")

        frame1.place(relx=0.0, rely=0.0, relheight=0.3, relwidth=0.5)
        frame2.place(relx=0.5, rely=0.0, relheight=0.3, relwidth=0.5)
        frame3.place(relx=0.0, rely=0.3, relheight=0.3, relwidth=0.5)
        frame4.place(relx=0.5, rely=0.3, relheight=0.3, relwidth=0.5)

        self.quitbutton = tk.Button(
            frame3, text="QUIT", fg="red", command=frame3.quit
        )
        self.quitbutton.place(relx=0.1, rely=0.1)

        self.handDisplay = HandDisplay(parent)
        self.handDisplay.place(relx=0.0, rely=0.6, relheight=0.4, relwidth=1.0)

    def setup_game(self):
        global game

        Player0 = ManualPlayer('zero')
        Player1 = ManualPlayer('uno')
        Player2 = ManualPlayer('zwei')
        Player3 = ManualPlayer('dries')

        game.add_player(Player0)
        game.add_player(Player1)
        game.add_player(Player2)
        game.add_player(Player3)

        game.deal()
        game.showhands()

        game.initialise_round(0, 0, 1)


class Window:

    def __init__(self, root):
        width = 1200
        height = 1200

        initialise_images()
        # set initial size of the window
        canvas = tk.Canvas(root, height=height, width=width)
        canvas.pack()

        app = App(root)


def initialise_images():
    # get card images
    global images, backs
    images = [[[] for j in range(13)] for i in range(4)]
    suits = ['H', 'S', 'D', 'C']
    values = [str(i) for i in range(2, 11)]
    values.extend(['J', 'Q', 'K', 'A'])
    for s in range(len(suits)):
        for v in range(len(values)):
            image_path = "images/" + values[v] + suits[s] + ".png"
            images[s][v] = tk.PhotoImage(file=image_path)
            images[s][v] = images[s][v].subsample(3)

    backs = [[] for i in range(len(colors))]
    for c in range(len(colors)):
        image_path = "images/" + colors[c] + "_back.png"
        backs[c] = tk.PhotoImage(file=image_path)
        backs[c] = backs[c].subsample(3)


if __name__ == "__main__":
    root = tk.Tk()

    window = Window(root)

    root.mainloop()
    root.destroy()
