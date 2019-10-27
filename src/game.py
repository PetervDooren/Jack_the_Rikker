import random
from collections import namedtuple

from player import Player

Card = namedtuple('Card', 'suit value')


class Game:
    def __init__(self):
        self._deck = []

        # initialise deck
        for suit in range(4):
            self._deck.extend([Card(suit, i) for i in range(2, 15)])
        random.shuffle(self._deck)

        # initialise player list
        self._players = []

        # round tracking
        self._starting_player = 0
        self._trump = -1
        self._rikker = -1
        self._mate = -1
        self.strokes_won = [0, 0, 0, 0]
        self.stroke_nr = 0

        # stroke tracking
        self.next_player = -1
        self.suit = None
        self.cards = [Card(0, 0) for i in range(4)]

    def add_player(self, player):
        assert isinstance(player, Player)
        nplayers = len(self._players)
        if nplayers < 4:
            player.id = nplayers
            self._players.append(player)
        else:
            print "Already four players added"

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

    def evaluate_stroke(self):
        if any([card.value == 0 for card in self.cards]):
            return

        highest_value = 0
        trumped = False
        victor = -1

        for pi in range(4):
            card = self.cards[pi]
            if card.suit == self._trump:
                if not trumped:
                    victor = pi
                    highest_value = card.value
                    trumped = True
                elif card.value > highest_value:
                    victor = pi
                    highest_value = card.value
            if card.suit == self.suit and not trumped:
                if card.value > highest_value:
                    victor = pi
                    highest_value = card.value
        return victor

    def initialise_stroke(self, starting_player):
        self.next_player = starting_player
        self.suit = None
        self.cards = [Card(0, 0) for i in range(4)]

    def initialise_round(self, rikker, trump, ace):
        self._rikker = rikker
        self._trump = trump
        print "{} is Rikking in {}".format(self._players[self._rikker].name, self._trump)

        self._find_mate(ace)
        print "{} is Mate with the ace of {}".format(self._players[self._mate].name, ace)

        self.strokes_won = [0, 0, 0, 0]

    def play(self, player_id, card):
        # verify input
        if player_id != self.next_player:
            print "It is currently not {}'s turn. {} is up next".format(
                self._players[player_id].name, self._players[self.next_player].name)
            return

        assert isinstance(card, Card), "invalid card type: {}" .format(card)

        # register card
        self.cards[player_id] = card

        if self.suit is None:
            self.suit = card.suit

        self.next_player = self.next_player + 1 if self.next_player < 3 else 0

        # verify stroke
        self.evaluate_stroke()

    def play_stroke(self):
        self.next_player = self._starting_player
        self.cards = [Card(0, 0) for i in range(4)]
        self.suit = None

        # play cards
        for i in range(4):
            p = self._players[self.next_player]
            card = p.play(self.suit)

            self.play(self.next_player, card)

            print "{} plays {}".format(p.name, card)

        return self.evaluate_stroke()

    def play_round(self, rikker, trump, ace):
        self.initialise_round(rikker, trump, ace)

        # play strokes
        for s in range(1, 14):
            print "Stroke {}".format(s)
            victor = self.play_stroke()
            print "winner is {}\n".format(self._players[victor].name)
            self.strokes_won[victor] += 1
            self._starting_player = victor

        print "strokes won:"
        for player in self._players:
            print "{} has won {} strokes".format(player.name, self.strokes_won[player.id])

    def _find_mate(self, ace):
        for player in self._players:
            if (ace, 13) in player._hand:
                self._mate = player.id
                return

    def _half_shuffle(self):
        #TODO implement half shuffle
        random.shuffle(self._deck)

    def showhands(self):
        for p in self._players:
            print p.name
            print p._hand
        print "\n"
