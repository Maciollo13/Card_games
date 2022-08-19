import cards
import random
import game_lib


class BJ_card(cards.Card):
    ACE_VALUE = 1

    def value(self):
        if self.face_up:
            v = cards.Card.RANKS.index(self.rank) + 1
            if v > 10:
                v = 10
        else:
            v = None
        return v


class BJ_deck(cards.Deck):
    def populate(self):
        for i in BJ_card.SUITS:
            for j in BJ_card.RANKS:
                self.cards.append(BJ_card(j, i))

class BJ_hand(cards.Hand):
    def __init__(self,name):
        super().__init__()
        self.name = name

    def __str__(self):
        rep = self.name + ":\t" + super().__str__()
        if self.total:
            rep += "(" + str(self.total) + ")"
            return rep

    @property
    def total(self):
        for card in self.cards:
            if not card.value:
                return None

        t = 0
        for i in self.cards:
            t += i.value

        contains_ace = False
        for card in self.cards:
            if card == BJ_card.ACE_VALUE:
                contains_ace = True

        if contains_ace and t < 11:
            t += 10
        return t

    def is_over(self):
        return self.total > 21


class BJ_player(BJ_hand):

    def is_drawing(self):
        response = game_lib.ask_yes_no("\n" + self.name + " - Do you want to draw a card. (Y/N)")
        return response == "y"

    def busted(self):
        print(self.name + " is busted")
        self.lose()

    def lose(self):
        print(self.name + " lost")

    def win(self):
        print(self.name + " won")

    def tie(self):
        print(self.name + " tied")