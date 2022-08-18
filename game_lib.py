class Player:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ":" + str(self.score)
        return rep

def ask_yes_no(question):
    response = ""
    while response not in ("y", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    response = None
    while response not in range(low, high+1):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("You must import this library,")
