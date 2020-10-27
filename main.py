print(" \t\t\t Welcome To Abhiyan's Rock Paper Scissors Game \t\t\t\n")
import random

attempts= 1
yourpoints=0
computerpoints=0

while(attempts<=10):

    list=["rock","paper","scissor"]
    ran= random.choice(list)
    print("What Do You Want To Choose rock,paper or scissor??")
    inp= input()

    if inp==ran:
        print("Tie")
        print(f"You Choose {inp} And Computer Choosed {ran}")
        print("Nobody Gets Point")

    elif inp=="rock" and ran=="scissor":
        yourpoints=yourpoints+1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Rock Smashes Scissor")
        print("You won This Round")
        print("Your Point Is ",yourpoints)

    elif inp == "scissor" and ran == "rock":
        computerpoints=computerpoints+1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Unlucky, Computer Won This Round")
        print("Computer's Point Is ", computerpoints)

    elif inp=="paper" and ran=="rock":
        yourpoints=yourpoints+1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Paper Pounce Rock")
        print("You Won This Round!!!")
        print("Your Point Is ",yourpoints)

    elif inp=="rock" and ran=="paper":
        computerpoints=computerpoints+1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Unlucky, Computer Won This Round")
        print("Computer Point Is ",computerpoints)

    elif inp == "scissor" and ran == "paper":
        yourpoints = yourpoints + 1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Scissor Cuts Paper")
        print("You Won This Round!!!")
        print("Your Point Is ", yourpoints)

    elif inp == "paper" and ran == "scissor":
        computerpoints = computerpoints + 1
        print(f"You Choosed {inp} And Computer Choosed {ran}")
        print("Unlucky, Computer Won This Round")
        print("Computer Point Is ", computerpoints)

    else:
        print("Input Invalid")