import random


class Player:
    def __init__(self, name):
        self.name = name
        self.id = -1
        self._hand = []

    def play(self):
        raise NotImplementedError

    def receive_hand(self, hand):
        self._hand = sorted(hand)


class AutoPlayer(Player):

    def play(self, suit):
        # check which cards are playable
        valid_cards = [card for card in self._hand if card.suit == suit]
        if not valid_cards:
            valid_cards = self._hand

        ind = int(random.random() * len(valid_cards))
        card = valid_cards[ind]
        self._hand.remove(card)
        return card


class ManualPlayer(Player):

    def play(self, ind, suit):
        card = self._hand[ind]
        # check which cards are playable
        valid_cards = [card for card in self._hand if card.suit == suit]
        if not valid_cards:
            valid_cards = self._hand

        if card in valid_cards:
            self._hand.remove(card)
            return card
        else:
            print "Invalid card selected {}"
            return None