import cards
import random
import game_lib


class BJ_card(cards.Card):
    ACE_VALUE = 1

    @property
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
    def __init__(self, name):
        super(BJ_hand,self).__init__()
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

    def is_busted(self):
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

class BJ_dealer(BJ_hand):
    def is_drawing(self):
        return self.total < 17

    def busted(self):
        print(self.name, "busted.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

class BJ_game(object):
    def __init__(self,names):
        self.players = []
        for name in names:
            player = BJ_player(name)
            self.players.append(player)
        self.dealer = BJ_dealer("Dealer")
        self.deck = BJ_deck()
        self.deck.populate()
        self.deck.shuffle()

    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def additional_cards(self,player):
        while not player.is_busted() and player.is_drawing:
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.busted()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand= 2)
        self.dealer.flip_first_card()
        for p in self.players:
            print(p)
        print(self.dealer)

        for p in self.players:
            self.additional_cards(p)

        self.dealer.flip_first_card()

        if not self.still_playing():
            print(self.dealer)
        else:
            print(self.dealer)
            self.additional_cards(self.dealer)
            if self.dealer.is_busted():
                for p in self.still_playing():
                    p.win()
            else:
                for p in self.still_playing():
                    if p.total > self.dealer.total:
                        p.win()
                    elif p.total == self.dealer.total:
                        p.tie()
                    else:
                        p.lose()

        for p in self.players:
            p.clear()

        self.dealer.clear()

def main():
    print("Welcome to the game of Black Jack! \n")
    names = []
    number = game_lib.ask_number("Enter the numbers of players (1 - 7) ",low= 1,high= 8)

    for i in range(number):
        name = input("Enter the name of the player: ")
        names.append(name)
    print()
    game = BJ_game(names)
    again = None
    while again != "n":
        game.play()
        again = game_lib.ask_yes_no("Do you want to continue? \n")
if __name__ == "__main__":
    main()