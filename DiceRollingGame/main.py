import random

def roll_dice():
    return random.randrange(1,6)

def game():
    x = input("Do you want to roll the dice? (y/n): ").lower()
    if x == 'y':
        print(f"You rolled a {roll_dice()}, {roll_dice()}")
        game()
    elif x == 'n':
        print("Thanks for playing!")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        game()

game()


