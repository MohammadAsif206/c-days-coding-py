# Number Guessing Game Objectives:
from art import logo
import random

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(logo)
secret_number = random.randint(1, 100)


def game_level():
    return input("Type hard for Hard mode in which you can have 5 guesses. \n"
                 "Type 'easy' for Easy mode in which you have 10 guess ")


def easy(secret):
    number_of_guess = 10
    for i in range(number_of_guess):
        print(f"You have {number_of_guess} attempts left")
        user_guess = int(input("Enter your guess: "))
        if user_guess == secret_number:
            print(f"You got it right! The answer was {secret}")
            break
        else:
            if user_guess < secret_number:
                print("Too low\n Guess again")
                number_of_guess -= 1
            else:
                print("Too high\n Guess again")
                number_of_guess -= 1


def hard(secret):
    number_of_guess = 5
    for i in range(number_of_guess):
        print(f"You have {number_of_guess} attempts left")
        user_guess = int(input("Enter your guess: "))
        if user_guess < 1 or user_guess > 100:
            print(f"You have entered {user_guess}; it is out of playing range. Enter a number between 1 and 100")
        else:
            if user_guess == secret_number:
                print(f"You got it right! The answer was {secret_number}")
                break
            else:
                if user_guess < secret_number:
                    print("Too low\n Guess again")
                    number_of_guess -= 1
                else:
                    print("Too high\n Guess again")
                    number_of_guess -= 1
            print("You've ran out of guesses, you lost.")


def play_game(level):
    if level == "easy":
        easy(secret_number)
    elif level == "hard":
        hard(secret_number)
    else:
        print(f"You have entered {game_level()}, it is not a valid playing mode: enter 'hard' or 'easy'")
        play_game(game_level())
    print("Thanks for playing our game, the program is closing....")


play_game(game_level())
