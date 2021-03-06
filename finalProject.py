"""Game of Trap
finalProject.py
Jacob Chotenovsky
Oct, 3 2017
Trap the Mystery Number
"""

#Setup variables#

count = 1

#Sets up the user by telling them what to do.#

print("Welcome to my game! \n \n In this guessing game, the computer generates a random number between 1 and 100. \n You will attempt to guess the number by entering two numbers - a lower boundary and an upper boundary. \n The computer will tell you if the mystery number is: \n smaller than the lower boundary,  \n greater than the upper boundary, \n or in between the two boundaries (ie, the number is trapped). \n To win the game, you must guess the mystery number by entering it as the same value for both of the boundaries. \n However you should not guess numbers more than, 100, less than 1, or with any decimal places.")
#Generates random number#

from random import randint
compfloat = float(randint(1, 100))
print (compfloat)

#Askes the user for it's guesses and if they are right or not#

while (count < 7):
    usernumlow = input("What is your low end guess?")
    usernumlow = float(usernumlow)
    usernumhigh = input("What is your high end guess?")
    usernumhigh = float(usernumhigh)
    count = count + 1
    if compfloat < usernumlow:
        print("The Mystery Number is lower than your lower boundary guess.")
    elif compfloat > usernumhigh:
        print("The Mystery Number is higher than your high boundary guess.")
    elif compfloat == usernumlow:
        if compfloat == usernumhigh:
            count = 41101
        else:
            print("The Mystery Number is between your high and low boundary guesses or on one of them.")
    else:
        print("The Mystery Number is between your high and low boundary guesses.")
if count == 7:
    print("Sorry, you lost.")
else:
    print("You trapped the Mystery Number!!")
