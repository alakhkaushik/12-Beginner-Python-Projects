from collections import UserString
import random


def play():
    userChoice = input(
        f"Enter r to choose Rock or p to choose Paper or s to choose Scissors: "
    )
    computerChoice = random.choice(["r", "p", "s"])
    print(f"Computer chose: {computerChoice}")
    getResults(userChoice, computerChoice)


def getResults(userChoice, computerChoice):
    # r>s, s>p, p>r
    if (userChoice == "r" and computerChoice == "s") or (
            userChoice == "s"
            and computerChoice == "p") or (userChoice == "p"
                                           and computerChoice == "r"):
        print("You win!")
    elif (computerChoice == "r"
          and userChoice == "s") or (computerChoice == "s" and userChoice
                                     == "p") or (computerChoice == "p"
                                                 and userChoice == "r"):
        print("Computer win!")
    else:
        print("It's a tie!")


if __name__ == "__main__":
    play()
