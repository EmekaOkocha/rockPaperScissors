import random

R = "Rock"
P = "Paper"
S = "Scissors"
count = 0
comp1 = ["R","P","S"]
player1 = ["R","P","S"]
comp = random.choice(comp1)
usersInput = input("Make a selection: R, P, S: ")
if ((usersInput == "R") or (usersInput == "P") or (usersInput == "S") ):
    if(comp == usersInput):
        print("Oops!!! There is a tie. Play again")
    else:
            print("Computer chose: " + comp +" And User chose: "+ usersInput)
else:
            print("Wrong input, Please choose R, P or S")
playAgain =input("Would you like to play again? Y/N")
while(count < 5):
    if(playAgain == "Y"):
        usersInput = input("Make a selection: R, P, S: ")
if ((usersInput == "R") or (usersInput == "P") or (usersInput == "S") ):
    if(comp == usersInput):
        print("Oops!!! There is a tie. Play again")
    else:
            print("Computer chose: " + comp +" And User chose: "+ usersInput)
else:
            print("Wrong input, Please choose R, P or S")
count +1
playAgain =input("Would you like to play again? Y/N")
