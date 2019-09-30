import random
from player import Player


class Game:
    def __init__(self):
        self._deck = []

        # initialise deck
        for suit in range(4):
            self._deck.extend([(suit, i) for i in range(2, 15)])
        random.shuffle(self._deck)

        # initialise player list
        self._players = []
        self._starting_player = 0

        # trump and teams
        self._trump = -1
        self._rikker = -1
        self._mate = -1

    def add_player(self, player):
        assert isinstance(player, Player)
        player.id = len(self._players)
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
        suit = None

        # play cards
        for i in range(4):
            p = self._players[pi]
            card = p.play(suit)

            if suit is None:
                suit = card[0]

            cards[pi] = card
            print "{} plays {}".format(p.name, card)
            pi = pi + 1 if pi < 3 else 0

        # evaluate results
        highest_value = 0
        trumped = False
        victor = -1
        for pi in range(4):
            card = cards[pi]
            if card[0] == self._trump:
                if not trumped:
                    victor = pi
                    highest_value = card[1]
                    trumped = True
                elif card[1] > highest_value:
                    victor = pi
                    highest_value = card[1]
            if card[0] == suit and not trumped:
                if card[1] > highest_value:
                    victor = pi
                    highest_value = card[1]
        return victor

    def play_round(self, rikker, trump, ace):
        self._rikker = rikker
        self._trump = trump
        print "{} is Rikking in {}".format(self._players[self._rikker].name, self._trump)

        self._find_mate(ace)
        print "{} is Mate with the ace of {}".format(self._players[self._mate].name, ace)

        strokes_won = [0, 0, 0, 0]

        # play strokes
        for s in range(1, 14):
            print "Stroke {}".format(s)
            victor = self.play_stroke()
            print "winner is {}\n".format(self._players[victor].name)
            strokes_won[victor] += 1
            self._starting_player = victor


        print "strokes won:"
        for player in self._players:
            print "{} has won {} strokes".format(player.name, strokes_won[player.id])

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
