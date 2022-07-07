import random


def guess(x):
    rand = random.randint(1, x)
    guess = 0
    while rand != guess:
        guess = int(input(f"Guess the number between 1 and {x}: "))
        if guess > rand:
            print(f"Guess is high")
        elif guess < rand:
            print(f"Guess is low")
        else:
            print(f"Thats's correct guess")
            break


def computerGuessed(SecretNumber):
    computerGuessed = random.randint(1, 100)
    while computerGuessed != SecretNumber:
        print(f"Computer gussed: {computerGuessed}")
        if computerGuessed > SecretNumber:
            print(f"Too high. Guess again:")
            computerGuessed = random.randint(1, computerGuessed - 1)
        elif computerGuessed < SecretNumber:
            print(f"Too low. Guess again:")
            computerGuessed = random.randint(computerGuessed + 1, SecretNumber)
    else:
        print(f"Bingo! {computerGuessed}")


if __name__ == "__main__":
    guess(100)
    computerGuessed(int(input(f"Set secret number between  1 to 100: ")))