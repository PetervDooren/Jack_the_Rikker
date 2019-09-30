import random


class Player:
    def __init__(self, name):
        self.name = name
        self.id = -1
        self._hand = []

    def play(self):
        ind = int(random.random() * len(self._hand))
        return self._hand.pop(ind)

    def receive_hand(self, hand):
        self._hand = sorted(hand)