import random


class Player:
    def __init__(self, name):
        self.name = name
        self.id = -1
        self._hand = []

    def play(self, color):
        # check which cards are playable
        valid_cards = [card for card in self._hand if card[0] == color]
        print "valid_cards for {}: {}".format(self.name, valid_cards)
        if not valid_cards:
            valid_cards = self._hand

        ind = int(random.random() * len(valid_cards))
        card = valid_cards[ind]
        self._hand.remove(card)
        return card

    def receive_hand(self, hand):
        self._hand = sorted(hand)