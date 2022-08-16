import random

class Player:

    def blast(self,enemy):
        score = random.randint(1,10)
        print("Player blasts Alien")
        if score > 3:
            enemy.die()
        else:
            enemy.win()


class Alien:

    def die(self):
        print("I'm dead x.x")

    def win(self):
        print("Ooops... Player missed\n"
              "Alien eats Player alive")


if __name__ == "__main__":
    player = Player()
    alien = Alien()
    player.blast(alien)