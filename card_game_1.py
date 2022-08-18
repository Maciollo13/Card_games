from random import shuffle



class Card:
    RANKS = ["A", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["♣", "♦", "♥", "♠"]

    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        rep = self.rank + self.suit
        return rep

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


class Unprintable_card(Card):
    def __str__(self):
        return "<secret>"

class Positionable_card(Card):
    def __init__(self,suit,rank,face_up= True):
        super().__init__(rank,suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Deck(Hand):
    def populate(self):
        for i in Card.SUITS:
            for j in Card.RANKS:
                self.add(Card(j,i))

    def shuffle(self):
        shuffle(self.cards)

    def deal(self, hands, per_hand=5):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card,hand)
                else:
                    print("Out of cards.")

if __name__ == "__main__":
    my_hand = Hand()
    your_hand =Hand()
    hands = [my_hand,your_hand]
    deck1 = Deck()
    deck1.populate()
    print(deck1)
    deck1.shuffle()
    print(deck1)
    deck1.deal(hands,per_hand=5)
    print(my_hand)
    print(your_hand)
    print(deck1)
    card1 = Card("A","♦")
    card2 = Unprintable_card("1","♦")
    card3 = Positionable_card("5","♦")
    card3.flip()
    print(card1,card2,card3)
