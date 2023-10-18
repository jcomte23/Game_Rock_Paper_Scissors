import game_options.functions.run_game as game

try:
    print()
    print(f"[ 🤖 Welcome to the game Rock, Paper, Scissors 🙋]")
    print()
    quantity_rounds = int(input("      How many rounds do you want to play? ->"))
    print()
    print(" " * 11, "Let's go, start the game.")
    print()

    game.run_game(quantity_rounds)
except ValueError:
    print(' ' * 13, "The quantity is invalid")
