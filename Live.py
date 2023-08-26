
import Score


def welcome(name):
    print("Please enter your name:")
    name = input()
    print(f"Hello {name} and welcome to the World of Games(WoG).\nHere you can find many cool games to play.")


def load_game():
    print("Please choose a game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 0.7 seconds and you have to guess it back\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS'")
    try:
        game_choice = int(input("Enter the number of the game you want to play: "))
        if game_choice < 1 or game_choice > 3:
            print("\n***Invalid input. Please enter a number of the game you want to play.***\n")
            return load_game()
    except ValueError:
        print("\n***Invalid input. Please enter a number of the game you want to play.***\n")
        return load_game()

    difficulty = int(input("Enter the difficulty level (1-5): "))
    if difficulty < 1 or difficulty > 5:
        print("Invalid difficulty level. Please enter a number between 1 and 5.")
        return load_game()

    if game_choice == 1:
        from MemoryGame import MemoryGame
        memory_game = MemoryGame(difficulty)
        win = memory_game.play()
    elif game_choice == 2:
        from GuessGame import GuessGame
        guess_game = GuessGame(difficulty)
        win = guess_game.play()
    elif game_choice == 3:
        from CurrencyRouletteGame import CurrencyRouletteGame
        currency_game = CurrencyRouletteGame(difficulty)
        win = currency_game.play()
    else:
        print("Invalid game choice.")
        return False

    if win:
        Score.add_score(difficulty)