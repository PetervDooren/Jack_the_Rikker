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
        self._starting_player = 0

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

    def play_stroke(self):
        pi = self._starting_player
        cards = [(0, 0) for i in range(4)]
        color = None

        # play cards
        for i in range(4):
            p = self._players[pi]
            card = p.play()

            if color is None:
                color = card[0]

            cards[pi] = card
            print "Player {} plays {}".format(p.name, card)
            pi = pi + 1 if pi < 3 else 0

        # evaluate results
        highest_value = 0
        victor = -1
        for pi in range(4):
            card = cards[pi]
            if card[0] == color:
                if card[1] > highest_value:
                    victor = pi
                    highest_value = card[1]

        print "Stroke 1"
        print "cards: {}".format(cards)
        print "Winner: {}".format(victor)

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

    game.play_stroke()
