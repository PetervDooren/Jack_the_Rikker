class Player:
    def __init__(self, name):
        self.name = name
        self._hand = []

    def play(self):
        return self._hand.pop()

    def receive_hand(self, hand):
        self._hand = sorted(hand)