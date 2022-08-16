



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

if __name__ == "__main__":
    card1 = Card(rank="A",suit="♣")
    card2 = Card(rank="2",suit="♣")
    card3 = Card(rank="3",suit="♣")
    card4 = Card(rank="4",suit="♣")
    card5 = Card(rank="5",suit="♣")
    my_hand = Hand()
    my_hand.add(card1)
    my_hand.add(card2)
    my_hand.add(card3)
    my_hand.add(card4)
    my_hand.add(card5)
