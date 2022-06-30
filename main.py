import random

R = "Rock"
P = "Paper"
S = "Scissors"
count = 0
comp1 = ["R","P","S"]
player1 = ["R","P","S"]
comp = random.choice(comp1)

def PlayAgain():
    rePlay =input("Would you like to play again? Y/N: ")
    if (rePlay == "y"):
        print("Lets try this one more time")
        PlayGame()
        if (rePlay == "n"):
            print("GAME OVER. THANKS FOR BEING A GOOD SPORTS")


def PlayGame():
    usersInput = input("Make a selection: R, P, S: ")
    if ((usersInput == "r") or (usersInput == "p") or (usersInput == "s") ):
        if(comp == usersInput):
            print("Oops!!! There is a tie. Play again")
        else:
            print("Computer chose: " + comp +" And User chose: "+ usersInput)
            PlayAgain()
    else:
            print("Wrong input, Please choose R, P or S")
            PlayAgain()


PlayGame()
