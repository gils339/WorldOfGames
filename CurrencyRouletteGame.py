# CurrencyRouletteGame.py
# This game will use the free currency api to get the current exchange rate from USD to ILS, will
# generate a new random number between 1-100 a will ask the user what he thinks is the value of
# the generated number from USD to ILS, depending on the user’s difficulty his answer will be
# correct if the guessed value is between the interval surrounding the correct answer
# Properties
# 1. Difficulty
# Methods
# 1. get_money_interval -Will get the current currency rate from USD to ILS and will
# generate an interval as follows:
# a. for given difficulty d, and total value of money t the interval will be: (t - (5 - d), t +
# (5 - d))
# 2. get_guess_from_user - A method to prompt a guess from the user to enter a guess of
# value to a given amount of USD
# 3. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won
import random
from currency_converter import CurrencyConverter


class CurrencyRouletteGame:
    list = []

    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.converter = CurrencyConverter()

        print("\nWelcome to the Currency Roulette Game!\n")

    def get_guess_from_user(self):
        try:
            return int(input("Enter your guess for the value in ILS: "))
        except ValueError:
            print("\nYou entered a wrong input, Please enter a number.\n")
            self.get_guess_from_user()

    def get_money_interval(self, usd):
        usd_to_ils = self.converter.convert(usd, 'USD', 'ILS')
        lower_interval = int(usd_to_ils -(5 - self.difficulty))
        higher_interval = int(usd_to_ils +(5 - self.difficulty))

        return lower_interval, higher_interval

    def is_between_interval(self,lower,higher,guess):
        is_between = guess >= lower and guess <= higher
        return is_between

    def play(self):
        usd_value = random.randint(1, 100)
        print(f"The value you need to convert to ILS from USD is: {usd_value}"'$')
        guess = self.get_guess_from_user()
        money_interval = self.get_money_interval(usd_value)
        between = self.is_between_interval(money_interval[0], money_interval[1], guess)
        if between:
            print("Congratulations! Your guess is within the correct range.")
            print(f"The actual value in ILS is {int(self.converter.convert(usd_value, 'USD', 'ILS'))}")
        else:
            print("Sorry, your guess is outside the correct range.")
            print(f"The actual value in ILS is {int(self.converter.convert(usd_value, 'USD', 'ILS'))}")
        return between
