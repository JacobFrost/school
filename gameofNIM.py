class Pile:
    def __init__(self, pile = 22):
        self.n_stickpile = pile

    def pileStatus(self):
        return self.n_stickpile

    def removeStickpile(self, amount):
        if amount < 5 and self.n_stickpile >= amount and amount > 0:
            self.n_sticks -= amount


class Player:
    def __init__(self, name = "Bob" , sticks = 0):
        self.sticks = sticks
        self.name = name

    def status(self):
        print(self.name + " Has ", self.n_sticks, "sticks.")

    def getName(self):
        return self.name
    
    def addSticks(self, amount):
        self.sticks += amount
    

class Game:
    def __init__(self):
        self.stickPile = Pile()
        self.player = Player(input("What is your name?"))
        self.ai = Player("Ai")


    def play(self):
            whostart = input("Who do you want to start? (0 for you, 1 for ai)")
            if whostart == "0":
                print("Great! You are starting first!")
                self.pickUpP()
            elif whostart == "1":
                print("Great! The computer will be starting first!")
                self.pickUpC()
            else:
                print("Sorry but that is not a valid choice.")


    def pickUpC(self):
        if self.stickPile != 0:
            winStrat = self.stickPile.pileStatus() % 5
            if winStrat != 0:
                self.pile.removeStickpile(winStrat)
                self.ai.addSticks(winStrat)
            else:
                sticks = randint(1,4)
                self.pile.removeStickpile(sticks)
                self.ai.addSticks(sticks)
            if self.stickPile == 0:
        else:
            self.win(player)

    def pickUpP(self):
        if
        while True:
            try:
                sticks = int(input(self.player.getName() + ", How many would you want to pick up?"))
                break
            except ValueError:
                print("That is not a valid integer number")
        print("You removed", sticks, "sticks from the pile.")
        self.pile.removeStickpile(sticks)


    def win(self, winner):
        print()


def start():
    game = Game()
    while True:
        print("""
    Welcome to the game of Nim!
    
    0 - Exit
    1 - Rules
    2 - Play
        """)
        choice = input("")
        if choice == "0":
            print("Thank you for playing the game.")
            exit()
        elif choice == "1":
            print("""
    The Rules
    
    The rules for the game of NIM are as follows:
    There are 22 sticks, beginning with either you or the computer, 1-4 sticks are chosen before the sides switch.
    This continues until there are no more sticks left. Whoever chose the last stick wins.
            """)
        elif choice == "2":
            print("Welcome to the game!")
            while True:
                game.play()
                break
start()
