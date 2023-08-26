# GuessGame.py
# The purpose of guess game is to start a new game, cast a random number between 1 to a
# variable called difficulty. The game will get a number input from the u
# Properties
# 1. Difficulty
# 2. Secret number
#
# Methods
# 1. generate_number - Will generate number between 1 to difficulty and save it to
# secret_number.
# 2. get_guess_from_user - Will prompt the user for a number between 1 to difficulty and
# return the number.
# 3. compare_results - Will compare the secret generated number to the one prompted
# by the get_guess_from_user.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.

import random


class GuessGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.secret_number = None

    def generate_number(self):
        self.secret_number = random.randint(1, self.difficulty)

    def get_guess_from_user(self):
        while True:
            try:
                guess = int(input("Enter a number between 1 and {}: ".format(self.difficulty)))
                if 1 <= guess <= self.difficulty:
                    return guess
                else:
                    print("Invalid input. Please enter a number between 1 and {}.".format(self.difficulty))
            except ValueError:
                print("Invalid input. Please enter a number.")

    def compare_results(self, guess):
        if guess == self.secret_number:
            print("Congratulations! You guessed the correct number.")
            return True
        elif guess < self.secret_number:
            print("You guessed too low. Try again.")
            return False
        else:
            print("You guessed too high. Try again.")
            return False

    def play(self):
        print("\nWelcome to the Guess Game!\n")
        self.generate_number()
        while True:
            guess = self.get_guess_from_user()
            if self.compare_results(guess):
                return True
