def run_game():
    computer_wins = 0
    user_wins = 0
    rounds = 1

    while True:
        if rounds <= quantity_rounds:
            print(" " * 8, '***' * 10)
            print(" " * 20, 'Round ', rounds)
            print(" " * 8, '***' * 10)
            print(" " * 3, f">>> Choose an option (Enter the name) <<<")
            rounds += 1

            user_option, computer_option = choose_options()
            print(user_option)
            print(computer_option)
        else:
            break


print()
print(f"[ 🤖 Welcome to the game Rock, Paper, Scissors 🙋]")
print()
# quantity_rounds = int(input("      How many rounds do you want to play? ->"))
quantity_rounds = 2
print()
print(" " * 11, "Let's go, start the game.")
print()
