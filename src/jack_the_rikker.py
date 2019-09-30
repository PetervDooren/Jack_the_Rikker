#!usr/bin/python
import random


class Game:
    def __init__(self):
        self._deck = []
        for color in range(4):
            self._deck.extend([(color, i) for i in range(2, 15)])

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
        return hands

    def shuffle(self):
        random.shuffle(self._deck)

    def half_shuffle(self):
        #TODO implement half shuffle
        random.shuffle(self._deck)


if __name__ == '__main__':
    game = Game()

    game.shuffle()
    hands = game.deal()
    for i in range(4):
        print "hand of player {}: \n {}".format(i, hands[i])
