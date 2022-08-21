from random import shuffle



class Card:
    RANKS = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self,rank,suit,face_up = True):
        self.rank = rank
        self.suit = suit
        self.face_up = face_up

    def __str__(self):
        if self.face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.face_up = not self.face_up

class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self,card):
        self.cards.append(card)

    def give(self,card , other_hand):
        self.cards.remove(card)
        other_hand.add(card)



class Deck(Hand):
    def populate(self):
        for i in Card.SUITS:
            for j in Card.RANKS:
                self.add(Card(j, i))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Out of cards.")



if __name__ == "__main__":
    print("This library contains Cards classes and functions.")