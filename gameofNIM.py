"""
This is a program that plays a game of NIM with the user. The goal of the game is to pick up the last stick.
Unless you can do mod calculations in your head you have a very good chance at loosing. Are you up to the challenge?
This ai is very good at winning so if you beat it you should definitely congratulate yourself.
Lauren Chotenovsky
March 29 2019
"""
from random import randint      # Imports random library


class Pile:                         # Creates the class Pile which is used to track and remove sticks from the pile
    def __init__(self, pile=22):       # Initializes self.pile to have a value of whatever is passed through or 22
        self.pile = pile

    def pileStatus(self):           # Returns the current size of the stick pile
        return self.pile

    def removepile(self, amount):   # Removes the amount that the ai or player removes from the pile
        self.pile -= amount


class Player:                       # Creates the class player which handles values for the ai and player
    def __init__(self, name="Bob", sticks=0):   # Initializes each player with default values if none are provided
        self.sticks = sticks
        self.name = name

    def getSticks(self):        # getSticks function returns the number of sticks the referred to player has
        return self.sticks

    def getName(self):          # getName function returns the name the referred to player
        return self.name
    
    def addSticks(self, amount):    # addSticks adds the amount of sticks taken from the pile to the player
        self.sticks += amount
    

class Game:                     # Creates the class Game which handles all the main game tasks
    def __init__(self):         # initializes the pile, player and ai to the appropriate classes
        self.pile = Pile()
        self.player = Player(input("What is your name?"))
        self.ai = Player("Ai")

    def play(self):                     # play function sets up who is playing first
        whostart = input("Who do you want to start? (0 for you, 1 for ai)")    # asks the user who they want to go first
        while True:
            if whostart == "0":
                print("\nGreat! You are starting first!")
                self.pickUpP()
                break
            elif whostart == "1":
                print("\nGreat! The computer will be starting first!")
                self.pickUpC()
                break
            else:
                print("Sorry but that is not a valid choice.")

    def pickUpC(self):      # sets up the function pickUpC with is picking up sticks for the ai
        amount = self.pile.pileStatus() % 5     # finds remainder of the pile divided by 5
        if amount != 0:                         # if it isn't 0 then it removes the mod amount from the pile
            self.pile.removepile(amount)
            self.ai.addSticks(amount)
        else:                                   # if the remainder is anything else then the ai removes a random amount
            amount = randint(1, 4)
            self.pile.removepile(amount)
            self.ai.addSticks(amount)
        print("The Ai took", amount, "from the pile\n")        # notifies the player of how much was taken
        if self.pile.pileStatus() == 0:                     # checks to see if the pile is empty, if so then the ai wins
            self.win("ai")
        else:
            self.pickUpP()              # changes to the players turn

    def pickUpP(self):      # sets up the function pickUpP with is picking up sticks for the player
        while True:         # gets the player to input a value, if it isnt an int then it loops
            try:
                print("You have", self.player.getSticks(), "sticks and the ai has", self.ai.getSticks(), "sticks.")
                amount = int(input(self.player.getName() + ", How many sticks do you want to pick up from"
                                                           " the " + str(self.pile.pileStatus()) + " stick pile?"))
                if amount <= 4:         # checks to see if the inputted value isn't too much or too little
                    if self.pile.pileStatus() >= amount:    # I couldn't shorten this code with &'s because it broke
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
        self.pile.removepile(amount)            # removes the sticks from the pile
        self.player.addSticks(amount)           # adds the sticks to the player
        if self.pile.pileStatus() == 0:         # checks to see if the pile is empty, if so then the player has won
            self.win("player")
        else:
            self.pickUpC()          # moves to the computers turn if the pile isnt empty

    def win(self, winner):      # creates the function win which takes an argument of a winner
        if winner == "player":  # if the winner is the player then it prints a message letting the user know
            print("Congrats " + self.player.getName() + ", you picked up the last stick and won!")
        elif winner == "ai":    # If the winner is the ai then it prints a message letting the user know
            print("Sorry " + self.player.getName() + ", the ai won.")


def start():        # This is the start of the game, allows the user to browse a menu and learn how the game works
    game = Game()   # sets up game to be linked to the Game class
    while True:     # prints a menu until the user leaves to play the game
        print("""
    Welcome to the game of Nim!
    
    0 - Exit
    1 - Rules
    2 - Play
        """)
        choice = input("")      # Lets the user choose if they want to exit, learn more or start
        if choice == "0":       # exits
            print("Thank you for playing the game.")
            break
        elif choice == "1":     # Teaches the user how to play the game
            print("""
    The Rules
    
    The rules for the game of NIM are as follows:
    There are 22 sticks, beginning with either you or the computer, 1-4 sticks are chosen before the sides switch.
    This continues until there are no more sticks left. Whoever chose the last stick wins.
            """)
        elif choice == "2":     # Starts the game
            print("Welcome to the game!")
            game.play()     # Calls the class game to use the function play which starts the game.
            break


start()
