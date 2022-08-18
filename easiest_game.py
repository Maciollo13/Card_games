import random
import game_lib

def main():
    print("Hello in Easiest Game.")
    again = None
    while again != "n":
        players = []
        num = game_lib.ask_number(question= "Input number of players (2-5) ",low=2,high=5)
        for i in range(num):
            name = input("Name: ")
            score = random.randint(1,100)
            player = game_lib.Player(name, score)
            players.append(player)
        print("Results:\n")
        for p in players:
            print(p)
        again = game_lib.ask_yes_no("Do you wish to play again? (y/n)")

if __name__ == "__main__":
    main()
