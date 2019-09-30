#!usr/bin/python
import random
from player import Player


class Game:
    def __init__(self):
        self._deck = []

        # initialise deck
        for color in range(4):
            self._deck.extend([(color, i) for i in range(2, 15)])
        random.shuffle(self._deck)

        # initialise player list
        self._players = []

    def add_player(self, player):
        assert isinstance(player, Player)
        self._players.append(player)

    def deal(self):
        hands = [[] for i in range(4)]

        for player in range(4):
            for card in range(6):
                hands[player].append(self._deck.pop())
        for player in range(4):
            for card in range(7):
                hands[player].append(self._deck.pop())

        if len(self._deck) != 0:
            print "Something went wrong with dealing!"

        for player in self._players:
            player.receive_hand(hands.pop())

    def _half_shuffle(self):
        #TODO implement half shuffle
        random.shuffle(self._deck)

    def showhands(self):
        for p in self._players:
            print p.name
            print p._hand


if __name__ == '__main__':
    game = Game()

    Player0 = Player('p0')
    Player1 = Player('p1')
    Player2 = Player('p2')
    Player3 = Player('p3')

    game.add_player(Player0)
    game.add_player(Player1)
    game.add_player(Player2)
    game.add_player(Player3)

    game.deal()
    game.showhands()