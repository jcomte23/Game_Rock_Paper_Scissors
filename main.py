import random


def choose_options():
    options = ("Rock", "Paper", "Scissors")
    print(' ' * 8, '🪨Rock, 📄Paper o ✂️Scissors')
    user_option = input(" " * 16 + "Option ->").capitalize().strip()
    if user_option in options:
        computer_option = random.choice(options)

        print(" " * 13, f"({user_option})", "VS", f"({computer_option})")
        return user_option, computer_option
    else:
        print(' ' * 13, "The name is invalid")
        return None, None


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print(" " * 20, 'Draw!')
        print(" " * 16, 'Nobody wins!\n')
    elif user_option == 'Rock':
        if computer_option == '️Scissors':
            print(" " * 10, '🪨 Rock beats scissors ✂️')
            print(" " * 15, '¡User wins!\n')
            user_wins += 1
        else:
            print(" " * 10, '📄 Paper beats a rock 🪨')
            print(" " * 15, '¡Computer wins!\n')
            computer_wins += 1
    elif user_option == 'Paper':
        if computer_option == 'Rock':
            print('📄 Paper beats rock 🪨')
            print('¡User wins!\n')
            user_wins += 1
        else:
            print('✂️ ️Scissors beats paper 📄')
            print('¡Computer wins!\n')
            computer_wins += 1
    elif user_option == '️Scissors':
        if computer_option == 'Rock':
            print('✂️ ️Scissors beats paper 📄')
            print('¡User wins!\n')
            user_wins += 1
        else:
            print('🪨 Rock beats ️scissors ✂️')
            print('¡Computer wins!\n')
            computer_wins += 1

    return user_wins, computer_wins


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
            user_wins, computer_wins = check_rules(user_option, computer_option, user_wins, computer_wins)
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

run_game()
