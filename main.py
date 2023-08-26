import Live

Live.welcome("")

while True:
    Live.load_game()
    play_again = input("Do you want to play another game? (y/n): ")
    if play_again.lower() != 'y':
        print("Goodbye!")
        break

