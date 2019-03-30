from random import randint

class Pile:
    def __init__(self, pile=22):
        self.pile = pile

    def pileStatus(self):
        return self.pile

    def removepile(self, amount):
        self.pile -= amount


class Player:
    def __init__(self, name="Bob", sticks=0):
        self.sticks = sticks
        self.name = name

    def getSticks(self):
        return self.sticks

    def getName(self):
        return self.name
    
    def addSticks(self, amount):
        self.sticks += amount
    

class Game:
    def __init__(self):
        self.pile = Pile()
        self.player = Player(input("What is your name?"))
        self.ai = Player("Ai")

    def play(self):
        whostart = input("Who do you want to start? (0 for you, 1 for ai)")
        if whostart == "0":
            print("\nGreat! You are starting first!")
            self.pickUpP()
        elif whostart == "1":
            print("\nGreat! The computer will be starting first!")
            self.pickUpC()
        else:
            print("Sorry but that is not a valid choice.")

    def pickUpC(self):
        amount = self.pile.pileStatus() % 5
        if amount != 0:
            self.pile.removepile(amount)
            self.ai.addSticks(amount)
        else:
            amount = randint(1, 4)
            self.pile.removepile(amount)
            self.ai.addSticks(amount)
        print("The Ai took", amount, "from the pile\n")
        if self.pile.pileStatus() == 0:
            self.win("ai")
        self.pickUpP()

    def pickUpP(self):
        while True:
            try:
                print("You have", self.player.getSticks(), "sticks and the ai has", self.ai.getSticks(), "sticks.")
                amount = int(input(self.player.getName() + ", How many sticks do you want to pick up from"
                                                           " the " + str(self.pile.pileStatus()) + " stick pile?"))
                if amount <= 4:
                    if self.pile.pileStatus() >= amount:
                        if amount >= 1:
                            break
                        else:
                            print("Sorry", amount, "is not a valid option. Please choose a value greater than"
                                                   " or equal to 1\n\n")
                    else:
                        print("Sorry", amount, "is not a valid option. Please choose a value less than"
                                               " or equal to the amount left in the pile.\n\n")
                else:
                    print("Sorry", amount, "is not a valid option. Please choose a value less than"
                                           " or equal to 4.\n\n")
            except ValueError:
                print("That is not a valid integer number\n\n")
        print("You removed", amount, "sticks from the pile.\n")
        self.pile.removepile(amount)
        self.player.addSticks(amount)
        if self.pile.pileStatus() == 0:
            self.win("player")
        self.pickUpC()

    def win(self, winner):
        if winner == "player":
            print("Congrats " + self.player.getName() + ", you picked up the last stick and won!")
        elif winner == "ai":
            print("Sorry " + self.player.getName() + ", the ai won.")
        exit()


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
