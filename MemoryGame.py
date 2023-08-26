# The purpose of memory game is to display an amount of random numbers to the users for 0.7
# seconds and then prompt them from the user for the numbers that he remember. If he was right
# with all the numbers the user will win otherwise he will lose.
# Properties
# 1. Difficulty
#
# Methods
# 1. generate_sequence - Will generate a list of random numbers between 1 to 101. The list
# length will be difficulty.
# 2. get_list_from_user - Will return a list of numbers prompted from the user. The list length
# twill be in the size of difficulty.
# # 3. is_list_equal - A function to compare two list if they are equal. The function will return
# True / False.
# 4. play - Will call the functions above and play the game. Will return True / False if the user
# lost or won.
import random
import time
import os


class MemoryGame:
    def __init__(self, difficulty):
        self.difficulty = difficulty

    def generate_sequence(self):
        sequence = [random.randint(1, 101) for _ in range(self.difficulty)]
        print("Remember the following numbers:")
        time.sleep(2)
        for number in sequence:
            print(number)
            time.sleep(0.7)
            os.system("clear")
        return sequence

    def get_list_from_user(self):
        user_input = input("Enter the numbers you remember: ")
        user_list = user_input.split()
        user_list = [int(num) for num in user_list]
        return user_list

    def is_list_equal(self, list1, list2):
        return list1 == list2

    def play(self):
        print("Welcome to the Memory Game!")
        sequence = self.generate_sequence()
        print("Time's up!")

        user_list = self.get_list_from_user()
        if self.is_list_equal(sequence, user_list):
            print("Congratulations! You won!")
            return True
        else:
            print("You lost, Try again.")
            return False

    def clear_console(self):
        pass





