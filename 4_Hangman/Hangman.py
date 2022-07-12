# from re import finditer
from Words import words
from HangmanVisuals import livesVisualDict
import random

if __name__ == "__main__":
    print("Welcome")
    wordToGuess = random.choice(words)
    wordToShow = len(wordToGuess) * "_"
    print(wordToGuess)
    life = len(livesVisualDict) - 1

    while life > 0 and wordToShow.__contains__("_"):
        userGuessedLetter = input(f"Guess the letter for {wordToShow}: ")
        if wordToGuess.__contains__(userGuessedLetter):
            # indices = [
            #     i.start() for i in finditer(userGuessedLetter, wordToGuess)
            # ]
            # print(indices)
            indices = [
                i for i, c in enumerate(wordToGuess) if c == userGuessedLetter
            ]

            for index in indices:
                wordToShow = wordToShow[:
                                        index] + userGuessedLetter + wordToShow[
                                            index + 1:]
            print("Bingo!")
        else:
            life -= 1
            print("Better luck next time!")

        print(livesVisualDict.get(life))
    else:
        if wordToShow.__contains__("_"):
            print("You have lost all your lives! =(")
        else:
            print(
                f"Congratulations, you won! The word you guessed is {wordToShow}."
            )

        # for letter in wordToGuess:
        #     if letter == userGuessedLetter:
        #         wordToShow =
