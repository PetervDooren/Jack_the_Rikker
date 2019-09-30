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

    game.play_round(0, 0, 1)
