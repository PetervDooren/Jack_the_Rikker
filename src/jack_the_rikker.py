#!usr/bin/python
from game import *

if __name__ == '__main__':
    game = Game()

    Player0 = Player('zero')
    Player1 = Player('uno')
    Player2 = Player('zwei')
    Player3 = Player('dries')

    game.add_player(Player0)
    game.add_player(Player1)
    game.add_player(Player2)
    game.add_player(Player3)

    game.deal()
    game.showhands()

    game.initialise_round(0, 0, 1)

    # play strokes
    for s in range(1, 14):
        print "Stroke {}".format(s)
        for i in range(4):
            p = game._players[game.next_player]
            card = p.play(game.suit)
            game.play(p.id, card)