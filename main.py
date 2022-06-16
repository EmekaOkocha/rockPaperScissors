import random

rock = "Rock"
paper = "Paper"
Scissors = "Scissors"
comp1 = ["R","P","S"]
player1 = ["R","P","S"]
comp = random.choice(comp1)
usersInput = input("Make a selection: R, P, S: ")
if (usersInput != rock or usersInput != paper or usersInput!= Scissors):
    print("Oops!!! Invalid Selection.Kindly choose R, P, or S.")
else:
        if comp != usersInput:
            print("we have a winner, your selection is: "+ " " + usersInput + "computer chose: "+ comp)
