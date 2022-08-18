import cards
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